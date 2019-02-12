

from bs4 import BeautifulSoup
import requests
import nltk
from nltk import corpus
import re

# url = "https://www.hindustantimes.com/tech/how-whatsapp-deals-with-spammers-automated-behaviour/story-FgqJaKQH7JK8is2SoUh5RO.html"

# url = "https://www.hindustantimes.com/tech/samsung-galaxy-s10-galaxy-s10-plus-rumour-round-up-foldable-phone-5g-price-features-specifications/story-yQLWD4EhgAJbnTkvwFjKSJ.html"

# url = "https://www.hindustantimes.com/tech/apple-sued-over-time-consuming-two-factor-authentication-on-iphone-mac/story-O234i3NBfjsr5hmQALgHjJ.html"

# url = "https://www.hindustantimes.com/tech/honor-view20-review-48-megapixel-camera-is-a-delight-but-there-s-more/story-anAz5iKDqAFZrDcv0ztbzH.html"

url = "https://www.hindustantimes.com/tech/vivo-v15-pro-with-32-megapixel-pop-up-selfie-camera-to-launch-in-india-on-february-20/story-GlFkEJUuEWFQlurYJr1QKM.html"

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


sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


print('executed3')
print()
print()

import heapq  
from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload()   


summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

print(summary_sentences)

def downloadimages(sent):
    arguments = {"keywords": sent , "format": "jpg", "limit":4, "print_urls":True, "size": "large", "aspect_ratio": "panoramic"}
    response.download(arguments)

# summary = ' '.join(summary_sentences)  
# print(summary)  
for sent in summary_sentences:
    print(sent)
    try:
        downloadimages(sent)
    except:
        print("some error")
    print()


import os
import glob
import shutil

# print(os.getcwd())
# os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\downloads")
# print(os.getcwd())
# fnames = []
# for file in os.listdir('.'):
#     fnames.append(file)
# # sort according to time of last modification/creation (os-dependent)
# # reverse: newer files first
# # fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)
# # # rename files, choose pattern as you like
# # for i, fname in enumerate(fnames): 
# #     print('changing folder names')    
# #     shutil.move(fname, "%03d_%s" % (i, fname))
# for files in fnames:
#     print(files)

# import os  
# os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader")


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
subfolders = [f.path for f in os.scandir("downloads") if f.is_dir() ]    

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


num = 0
for i in subfolders:
    caption = exact_name(i)
    caption_first_arr = caption.split()[:8]
    caption_second_arr = caption.split()[8:16]
    caption_third_arr = caption.split()[16:]

    caption_first  = " ".join(caption_first_arr)
    caption_second = " ".join(caption_second_arr)
    caption_third = " ".join(caption_third_arr)
    
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
            font = ImageFont.truetype("Arial Bold.ttf", 30)
            if count == 0:
                    draw.text(( new_width/10 + 60, new_height - 100), caption_first, (255,0,0),font=font, align="center")
            elif count == 1:
                draw.text(( new_width/10 + 60, new_height - 100),caption_second, (255,0,0),font=font, align="center")  
            else:
                draw.text(( new_width/10 + 60, new_height - 100),caption_third, (255,0,0),font=font, align="center")                
        
            # draw.text((x, y),"Sample Text",(r,g,b))
            # if display3:
            #     if count == 0:
            #           draw.text(( new_width/10 + 60, new_height - 100), caption_first, (255,0,0),font=font, align="center")
            #     elif count == 1:
            #         draw.text(( new_width/10 + 60, new_height - 100),caption_second, (255,0,0),font=font, align="center")  
            #     else:
            #         draw.text(( new_width/10 + 60, new_height - 100),caption_third, (255,0,0),font=font, align="center")                
            # if display2:
            #     if count == 0:
            #           draw.text(( new_width/10 + 60, new_height - 100), caption_first, (255,0,0),font=font, align="center")
            #     elif count == 1:
            #         draw.text(( new_width/10 + 60, new_height - 150),caption_second , (255,0,0),font=font, align="center")  
            #         draw.text(( new_width/10 + 60, new_height - 100),caption_third, (255,0,0),font=font, align="center")            
            # if display1:
            #     if count == 0:
            #         draw.text(( new_width/10 + 60, new_height - 150), caption_first, (255,0,0),font=font, align="center")
            #         draw.text(( new_width/10 + 60, new_height - 100), caption_second, (255,0,0),font=font, align="center")
            #         draw.text(( new_width/10 + 60, new_height - 50),caption_third, (255,0,0),font=font, align="center")            
                
            # img.show()
            img.save("newfolder/{}".format(f))        
            print('done')
            count = count + 1
    print()


import glob
import os
import shutil


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

import os
import cv2
from PIL import Image

def generate_video():
    os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder2")

    image_folder = '.' #make sure to use your folder
    video_name = 'videos4.avi'

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]
    print(images)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


path = "f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder"

dirs = os.listdir(path)
print(dirs)


def resize():
    for item in dirs:
        im = Image.open(os.path.join(path, item))
        width, height = im.size
        print(width, height)
        # f, e = os.path.splitext(path+item)
        imResize = im.resize((1200,450), Image.ANTIALIAS)
        imResize.save( "newfolder2/" + item + ' resized.jpg', 'JPEG', quality=95)
        print('done')
    generate_video()

resize()





        



