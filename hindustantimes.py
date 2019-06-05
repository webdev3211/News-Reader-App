
import shutil
import os
import glob
import numpy as np 

from bs4 import BeautifulSoup
import requests
import nltk
from nltk import corpus
import re

from flask import Flask, render_template, request, jsonify, url_for  
app = Flask(__name__)


from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload()   

from gtts import gTTS 
language = 'en'

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import cv2
import heapq  


from flask import request
from flask import jsonify
from flask import Flask



app = Flask(__name__)

if os.path.isdir("f:\\xampp\\htdocs\\Python\\NewsReader\\downloads"):
    shutil.rmtree('f:\\xampp\\htdocs\\Python\\NewsReader\\downloads')
if os.path.isdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder"):
    shutil.rmtree('f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder')

os.mkdir("newfolder")


def exact_name(name):
    return name[10:]

def ext(url):
    index = url.find(".jpg")
    current_url = ""
    current_url = url[index:]
    return current_url   

def ext2(url):
    index = url.find(".jpeg")
    current_url = ""
    current_url = url[index:]
    return current_url   

def ext3(url):
    index = url.find(".png")
    current_url = ""
    current_url = url[index:]
    return current_url  

def convert(words):
    s = ""
    for word in words:
        s += word.upper() 
    return s

def downloadimages(sent, article_heading):
    arguments = {"keywords": sent, "format": "jpg", "limit":4, "print_urls":True, "size": "medium",  "suffix_keyword": article_heading}
    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {"keywords": sent, "format": "jpg", "limit":4, "print_urls":True, "size": "medium",  "suffix_keyword": article_heading}
        try:
            response.download(arguments)
        except:
            pass

#flask

@app.route('/', methods=['POST', 'GET'])
def newsreader():
    if request.method=='POST':
        # input_json = request.get_json(force=True)
        # print(request.form)
        url = request.form.get('url')
        print(url)
        box = request.form.get('check1')
        print(box)

        if(url[0:30] != "https://www.hindustantimes.com"):
            response = {
                'Error': 'Invalid url given, kindly give page url from hindustantimes website newspage'
            }
            return jsonify(response)
        

        source = requests.get(url).text

        soup = BeautifulSoup(source, 'lxml')

        # print(soup.prettify().encode('utf-8'))
        str = ""
        for div in soup.find_all('div', attrs = {'class':'story-details'}):
            for p in div.findChildren('p'):
                try:
                    str  = str + p.text
                except:
                    pass

        heading = ""
        div = soup.find('div', attrs = {'class':'story-highlight'})
        h1 = div.findChild()
        heading = h1.text

        article_heading = re.sub('[^A-Za-z0-9.]+', ' ', heading)

        article_text = re.sub('[^A-Za-z0-9.]+', ' ', str)
        # newstr = re.sub(r'\s+', ' ', str)

        print(article_heading)
        print()
        print(article_text)


        sentence_list = nltk.sent_tokenize(article_text) 

        stopwords = nltk.corpus.stopwords.words('english')

        word_frequencies = {}  
        for word in nltk.word_tokenize(article_text):  
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1


        print('executed1')
        maximum_frequncy = max(word_frequencies.values())

        for word in word_frequencies.keys():  
            word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

        print('executed2')
        print('executed 5')


        sentence_scores = {}  
        for sent in sentence_list:  
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]

        
        summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

        print(summary_sentences)

        print('executed3')
        print()
        print()




        audio_text = "The news headline is  " + article_heading  + ',  ,'
        for line in summary_sentences:
            audio_text += line
            audio_text + ',    ,'

        
        if box == 'Audio':
            myobj = gTTS(text=audio_text, lang=language, slow=False) 
            myobj.save("newsaudio.mp3")
            response = {
                'Output': 'Audio Generated check your folder now'
            }
            os.system("start F:/xampp/htdocs/Python/NewsReader/newsaudio.mp3")
            return jsonify(response)

        else:
            # summary = ' '.join(summary_sentences)  
            # print(summary)  
            for sent in summary_sentences:
                downloadimages(sent ,article_heading)  
                print()


            subfolders = [f.path for f in os.scandir("downloads") if f.is_dir() ]    


            num = 0
            for i in subfolders:
                caption = exact_name(i)
                caption_first_arr = caption.split()[:8]
                caption_second_arr = caption.split()[8:16]
                caption_third_arr = caption.split()[16:]

                caption_first  = " ".join(caption_first_arr)
                caption_second = " ".join(caption_second_arr)
                caption_third = " ".join(caption_third_arr)
                
                caption_first = convert(caption_first)
                caption_second = convert(caption_second)
                caption_third = convert(caption_third)
                

                count = 0

                list = os.listdir(i) # dir is your directory path
                number_files = len(list)

                display1 = False
                display2 = False
                display3 = False

                if number_files >= 3:
                    display3 = True
                if number_files == 2 :
                    display2 = True
                if number_files == 1:
                    display1 = True
                    
                print(display1)
                print(display2)
                print(display3)
                
                for f in os.listdir(i):
                    try:
                        if (ext(f) == '.jpg' or ext2(f) == '.jpeg' or ext3(f) == '.png'):
                            print(f)
                            img = Image.open(os.path.join(i, f))    
                            width, height = img.size
                            basewidth = 1200
                            # print(height)
                            wpercent = (basewidth/float(img.size[0]))
                            hsize = int((float(img.size[1])*float(wpercent)))
                            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                            new_width, new_height = img.size
                            # print(new_height)
                            if not img.mode == 'RGB':
                                img = img.convert('RGB')
                        
                            draw = ImageDraw.Draw(img)
                            # font = ImageFont.truetype(<font-file>, <font-size>)
                            font = ImageFont.truetype("Arial Bold.ttf", 32)
                            # if count == 0:
                            #         draw.text(( new_width/10 + 60, new_height - 100), caption_first, (255,0,0),font=font, align="center")
                            # elif count == 1:
                            #     draw.text(( new_width/10 + 60, new_height - 100),caption_second, (255,0,0),font=font, align="center")  
                            # else:
                            #     draw.text(( new_width/10 + 60, new_height - 100),caption_third, (255,0,0),font=font, align="center")                

                            # draw.text((x, y),"Sample Text",(r,g,b))
                            if display3:
                                if count == 0:
                                    draw.text(( new_width/20 + 10, new_height - 100), caption_first, (255,0,0),font=font, align="center")
                                elif count == 1:
                                    draw.text(( new_width/20 + 10, new_height - 100),caption_second, (255,0,0),font=font, align="center")  
                                else:
                                    draw.text(( new_width/20 + 10, new_height - 100),caption_third, (255,0,0),font=font, align="center")                
                            if display2:
                                if count == 0:
                                    draw.text(( new_width/20 + 10, new_height - 100), caption_first, (255,0,0),font=font, align="center")
                                elif count == 1:
                                    draw.text(( new_width/20 + 10, new_height - 150),caption_second , (255,0,0),font=font, align="center")  
                                    draw.text(( new_width/20 + 10, new_height - 100),caption_third, (255,0,0),font=font, align="center")            
                            if display1:
                                if count == 0:
                                    draw.text(( new_width/20 + 10, new_height - 150), caption_first, (255,0,0),font=font, align="center")
                                    draw.text(( new_width/20 + 10, new_height - 100), caption_second, (255,0,0),font=font, align="center")
                                    draw.text(( new_width/20 + 10, new_height - 50),caption_third, (255,0,0),font=font, align="center")            
                                
                            # img.show()
                            # imResize = im.resize((1200,450), Image.ANTIALIAS)    
                            img.save("newfolder/{}".format(f))        
                            print('done')
                            count = count + 1
                    except OSError:
                        pass
                print()



            os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\downloads")

            fnames = []
            for file in os.listdir('.'):
                fnames.append(file)

            fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)

            for files in fnames:
                print(files)



            print(os.getcwd())
            os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder")
            print(os.getcwd())

            # get a list of all txt files

            # fnames = glob.glob("*.jpg")
            fnames2 = []
            for files in os.listdir('.'):
                fnames2.append(files)
            # sort according to time of last modification/creation (os-dependent)
            # reverse: newer files first
            fnames2.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)
            # rename files, choose pattern as you like
            for i, fname in enumerate(fnames2):
                print(fname + ' : is changed ')    
                shutil.move(fname, "img-%03d%s" % (i, ".jpg"))

            # fnames2 = glob.glob("*.jpeg")
            # fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)

            for files in os.listdir('.'):
                print(files)

            # sort according to time of last modification/creation (os-dependent)
            # reverse: newer files first



            os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder")

            path = "f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder"

            dirs = os.listdir(path)
            print(dirs)
            mean_width = 0
            mean_height = 0

            num_of_images = len(os.listdir('.'))

            for file in os.listdir('.'):
                try:
                    im = Image.open(os.path.join(path, file))
                    width, height = im.size
                    mean_width += width
                    mean_height += height
                except OSError:
                    pass
            mean_width = int(mean_width/num_of_images)
            mean_height = int(mean_height/num_of_images)
            print(mean_width, mean_height)


            for item in dirs:
                try:
                    im = Image.open(os.path.join(path, item))
                    width, height = im.size
                    print(width, height)
                    # f, e = os.path.splitext(path+item)
                    imResize = im.resize((mean_width,mean_height), Image.ANTIALIAS)
                    imResize.save( item , 'JPEG', quality=95)
                    print('done')
                except OSError: 
                    pass



            os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder")


            image_folder = '.' #make sure to use your folder
            video_name = 'generated.avi'


            images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]
            print(images)
            frame = cv2.imread(os.path.join(image_folder, images[0]))
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width,height))

            for image in images:
                video.write(cv2.imread(os.path.join(image_folder, image)))

            cv2.destroyAllWindows()
            video.release()

            response = {
                'Output': 'Video Generated check your folder now'
            }

            # # Create a VideoCapture object and read from input file 
            # cap = cv2.VideoCapture('generated.avi') 

            # # Check if camera opened successfully 
            # if (cap.isOpened()== False): 
            #     print("Error opening video file") 

            # # Read until video is completed 
            # while(cap.isOpened()): 
            #     # Capture frame-by-frame 
            #     ret, frame = cap.read() 
            #     if ret == True: 
            #         cv2.imshow('Frame', frame) 
            #         # Press Q on keyboard to exit 
            #         if cv2.waitKey(1500) & 0xFF == ord('q'): 
            #             break
            #     else: 
            #         break

            # # When everything done, release 
            # # the video capture object 
            # cap.release() 

            # # Closes all the frames 
            # cv2.destroyAllWindows() 
            os.system("start F:/xampp/htdocs/Python/NewsReader/newfolder/generated.avi")


            return jsonify(response)

    return render_template('home.html')



if __name__ == '__main__':
    app.run(port=9000, debug=True)


