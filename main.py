

from bs4 import BeautifulSoup
import requests
import nltk
from nltk import corpus
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import os
import cv2



def exact_url(url):
    index = url.find(".html")
    index = index + 5
    current_url = ""
    current_url = url[:index]
    return current_url


url = "https://www.nytimes.com/2019/02/03/world/middleeast/pope-francis-uae-mideast-muslims.html"

news_url = exact_url(url)

source = requests.get(news_url).text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify().encode('utf-8'))
str = ""
for para in soup.find_all('p', attrs = {'class':'css-1ygdjhk evys1bk0'}):
    str = str + para.text
   
# print(str)


article_text = re.sub('[^A-Za-z0-9.]+', ' ', str)
# newstr = re.sub(r'\s+', ' ', str)

# print(article_text)
print()

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


summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

print(summary_sentences)

def downloadimages(sent):
    arguments = {"keywords": sent ,"limit":4,"print_urls":True}  
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




subfolders = [f.path for f in os.scandir("downloads") if f.is_dir() ]    

def exact_name(name):
    return name[10:]


for i in subfolders:
    caption = exact_name(i)
    for f in os.listdir(i):
        img = Image.open(os.path.join(i, f))    
        basewidth = 1000
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        if not img.mode == 'RGB':
            img = img.convert('RGB')
        try:
            draw = ImageDraw.Draw(img)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("arial.ttf", 15)
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw.text((50,50), caption ,(255,0,0),font=font, align="center")
        except:
            pass
        img.save("newfolder/{}".format(f))
        # img.show()
        print('done')
        


