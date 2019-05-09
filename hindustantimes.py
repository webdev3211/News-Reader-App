
import shutil
import os

if os.path.isdir("f:\\xampp\\htdocs\\Python\\NewsReader\\downloads"):
    shutil.rmtree('f:\\xampp\\htdocs\\Python\\NewsReader\\downloads')
if os.path.isdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder"):
    shutil.rmtree('f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder')

os.mkdir("newfolder")

from bs4 import BeautifulSoup
import requests
import nltk
from nltk import corpus
import re

# url = "https://www.hindustantimes.com/india-news/feb-14-kashmir-blast/story-AoDEbZlMmvU6rHj6mwDDHO.html"

# url = "https://www.hindustantimes.com/tech/vivo-v15-pro-with-32-megapixel-pop-up-selfie-camera-to-launch-in-india-on-february-20/story-GlFkEJUuEWFQlurYJr1QKM.html"

# url = "https://www.hindustantimes.com/tech/samsung-to-refresh-galaxy-a-series-with-phones-priced-between-rs-10-000-and-rs-50-000/story-qc9DZXT0rOu8kKItwI9yoL.html"
url = "https://www.hindustantimes.com/india-news/44-crpf-jawans-killed-in-worst-terror-attack-in-kashmir-india-slams-pakistan/story-wCajHcY345jfHuflowa4pN.html"

# url = "https://www.hindustantimes.com/tech/realme-3-to-launch-in-india-next-month-takes-on-xiaomi-redmi-note-7/story-dwr10nRWh2VaTGerxPvh9O.html"

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

import heapq  

summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

print(summary_sentences)

print('executed3')
print()
print()


from google_images_download import google_images_download   
response = google_images_download.googleimagesdownload()   



audio_text = ""
for line in summary_sentences:
    audio_text += line

print(audio_text)


from gtts import gTTS 

language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=audio_text, lang=language, slow=False) 
  
myobj.save("welcome2.mp3") 


def downloadimages(sent):
    arguments = {"keywords": sent, "format": "jpg", "limit":4, "print_urls":True, "size": "medium",  "suffix_keyword": article_heading}
    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {"keywords": sent, "format": "jpg", "limit":4, "print_urls":True, "size": "medium",  "suffix_keyword": article_heading}
        try:
            response.download(arguments)
        except:
            pass

# summary = ' '.join(summary_sentences)  
# print(summary)  
for sent in summary_sentences:
    downloadimages(sent)  
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

def convert(words):
    s = ""
    for word in words:
        s += word.upper() 
    return s


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

import os

import glob
import shutil


os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\downloads")

fnames = []
for file in os.listdir('.'):
    fnames.append(file)

fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)

for files in fnames:
    print(files)



import os

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
from PIL import Image

os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder")

path = "f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder"

dirs = os.listdir(path)
print(dirs)
mean_width = 0
mean_height = 0

num_of_images = len(os.listdir('.'))

for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width += width
    mean_height += height

mean_width = int(mean_width/num_of_images)
mean_height = int(mean_height/num_of_images)
print(mean_width, mean_height)


for item in dirs:
    im = Image.open(os.path.join(path, item))
    width, height = im.size
    print(width, height)
        # f, e = os.path.splitext(path+item)
    imResize = im.resize((mean_width,mean_height), Image.ANTIALIAS)
    imResize.save( item , 'JPEG', quality=95)
    print('done')

def pypart(n): 
	for i in range(0, n): 
		for j in range(0, i+1):
		    if j == 0:
		        print('Generating video', end='')
		    print(". ",end="") 
		print("\n") 



import cv2
import os
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



# from gtts import gTTS 

# language = 'en'
  
# # Passing the text and language to the engine,  
# # here we have marked slow=False. Which tells  
# # the module that the converted audio should  
# # have a high speed 
# myobj = gTTS(text=audio_text, lang=language, slow=False) 
  
# myobj.save("welcome2.mp3") 