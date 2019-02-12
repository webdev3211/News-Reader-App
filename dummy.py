# # from google_images_download import google_images_download   #importing the library

# # response = google_images_download.googleimagesdownload()   #class instantiation

# # arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
# # paths = response.download(arguments)   #passing the arguments to the function
# # print(paths)   #printing absolute paths of the downloaded images



# # print("Hello")

# import cv2
# import os

# image_folder = '.' #make sure to use your folder
# video_name = 'videos4.avi'

# images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]
# print(images)
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape

# video = cv2.VideoWriter(video_name, 0, 1, (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()
# print('done')
# import path


# import glob
# import os

# search_dir = "downloads/"
# # remove anything from the list that is not a file (directories, symlinks)
# # thanks to J.F. Sebastion for pointing out that the requirement was a list 
# # of files (presumably not including directories)  
# files = filter(os.path.isfile, glob.glob(search_dir + "*"))
# files.sort(key=lambda x: os.path.getmtime(x))

# print(files)


# dirpath = "downloads"

# def getfiles(dirpath):
#     a = [s for s in os.listdir(dirpath)
#          if os.path.isfile(os.path.join(dirpath, s))]
#     a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
#     return a


# from PIL import Image, ImageDraw, ImageFont
# import os

# img = Image.open("sample_in.jpg")    
# basewidth = 850
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# draw = ImageDraw.Draw(img)
# # font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("arial.ttf", 20)
# # draw.text((x, y),"Sample Text",(r,g,b))
# draw.text((50,350), "this is the subtitle" ,(255,255,255,100),font=font, align="center")
# f  = "thisisme.jpg"
# img.save("newfolder/{}".format(f))
# # img.show()
# print('done')

# from PIL import Image, ImageDraw

# im = Image.open("sample_in.jpg")

# draw = ImageDraw.Draw(im)
# draw.line((0, 0) + im.size, fill=128)
# draw.line((0, im.size[1], im.size[0], 0), fill=128)
# im.show()
# print("done")

# # write to stdout





# import cv2
# import os

# image_folder = 'newfolder' #make sure to use your folder
# video_name = 'mvideo.avi'

# images = [img for img in os.listdir(image_folder)]
# for img in images:
#     print(img)
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape
# print(frame.shape)

# video = cv2.VideoWriter(video_name, 0, 1, (width,height))

# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))
#     print('done')

# cv2.destroyAllWindows()
# video.release()




# from os import path


# def exact_name(name):
#     return name[10:]

# def ext(url):
#     index = url.find(".jpg")
#     current_url = ""
#     current_url = url[index:]
#     return current_url   
# num = 0
# for i in subfolders:
#     for f in os.listdir(i):
#         if (ext(f) == '.jpg'):
#             src = os.path.abspath(f)
#             # src = path.realpath(f)

#             # print(f)
#             # src1 = src.split('\\')[:5]
#             # source = "\\".join(src1)
#             # filenm = src.split('\\')[5:]
#             # filename = "".join(filenm)
#             # dst ="photo" + str(num) + ".jpg"
#             # img_src = source + '\\' + filename 
#             print(os.path.isfile(src))            
#             # dst = source + '\\' + dst
#             # # dst = os.path.join(source, dst)            
#             # print(dst)
#             # os.rename(src, dst) 
#             # print(dst)
#             num += 1
            

import os
import glob
import shutil


# fnames = [f.path for f in os.scandir("downloads") if f.is_dir() ]    

# 
# os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\downloads")
# 
# fnames = []
# for file in os.listdir('.'):
#     fnames.append(file)
# # sort according to time of last modification/creation (os-dependent)
# # reverse: newer files first
# fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)
# # rename files, choose pattern as you like
# for i, fname in enumerate(fnames): 
#     print('changing folder names')    
#     shutil.move(fname, "%03d_%s" % (i, fname))

# print(fnames[0])


# def exact_name(name):
#     return name[14:]


# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw 
# import os
# subfolders = [f.path for f in os.scandir("downloads") if f.is_dir() ]    

# def exact_name(name):
#     return name[14:]

# def ext(url):
#     index = url.find(".jpg")
#     current_url = ""
#     current_url = url[index:]
#     return current_url   
# num = 0
# for i in subfolders:
#     caption = exact_name(i)
#     caption_first_arr = caption.split()[:7]
#     caption_second_arr = caption.split()[7:14]
#     caption_third_arr = caption.split()[14:]

#     caption_first  = " ".join(caption_first_arr)
#     caption_second = " ".join(caption_second_arr)
#     caption_third = " ".join(caption_third_arr)
#     count = 0
    
#     for f in os.listdir(i):
#         if (ext(f) == '.jpg'):
#             try:
#                 img = Image.open(os.path.join(i, f))    
#                 width, height = img.size
#                 basewidth = 1200
#                 # print(height)
#                 wpercent = (basewidth/float(img.size[0]))
#                 hsize = int((float(img.size[1])*float(wpercent)))
#                 img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#                 new_width, new_height = img.size
#                 # print(new_height)
#                 # if not img.mode == 'RGB':
#                 #     img = img.convert('RGB')
            
#                 draw = ImageDraw.Draw(img)
#                 # font = ImageFont.truetype(<font-file>, <font-size>)
#                 font = ImageFont.truetype("Arial Bold.ttf", 30)
#                 # draw.text((x, y),"Sample Text",(r,g,b))
#                 if count == 0:
#                     draw.text(( new_width/10 + 65, new_height - 100), caption_first, (0,0,0),font=font, align="center")
#                 elif count == 1:
#                     draw.text(( new_width/10 + 65, new_height - 100),caption_second, (0,0,0),font=font, align="center")  
#                 else:
#                     draw.text(( new_width/10 + 65, new_height - 100),caption_third, (0,0,0),font=font, align="center")                
                              
#             except:
#                 pass
#             # img.show()
#             img.save("newfolder/{}".format(f))        
#             print('done')
#             count = count + 1




# # 
# # os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder")
# # 

# # # get a list of all txt files
# # fnames = glob.glob("*.jpg")
# # # sort according to time of last modification/creation (os-dependent)
# # # reverse: newer files first
# # fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)
# # # rename files, choose pattern as you like
# # for i, fname in enumerate(fnames):
# #     print('changing name')    
# #     shutil.move(fname, "%03d_%s" % (i, fname))
        
 
 # Python program to rename all file 
# # names in your directory  
# import os 
  
# os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder")
#  
# COUNT = 100
  
# # Function to increment count  
# # to make the files sorted. 
# def decrement(): 
#     global COUNT 
#     COUNT = COUNT - 1
  
  
# for f in os.listdir(): 
#     f_name, f_ext = os.path.splitext(f) 
#     f_name = "photo" + str(COUNT) 
#     decrement() 
  
#     new_name = '{} {}'.format(f_name, f_ext) 
#     os.rename(f, new_name) 
#     print(new_name)



# import os
# import glob
# import shutil


# os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\downloads")

# fnames = []
# for file in os.listdir('.'):
#     fnames.append(file)

# fnames.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)

# for files in fnames:
#     print(files)
# import re
# query = "pm modi lifestyle"




# def querystring():
#     arr = query.split(' ')
#     str = ""
#     n = len(arr)
#     for i in arr:
#         str += i + "+"

#     str2 = ""
#     count = len(str) - 1
#     i = 0
#     while(i<count):
#         str2 += str[i]
#         i += 1
#     return str2

# query = querystring()

# url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_nsDoz7XgAhUUXn0KHYpOA0MQ_AUIDygC&biw=1366&bih=635"

# print(url)

# from bs4 import BeautifulSoup
# import requests

# source = requests.get(url).text

# soup = BeautifulSoup(source, 'lxml')
# for div in soup.find_all('div'):
#     print(div)



# import cv2
# import os

# image_folder = 'newfolder' #make sure to use your folder
# video_name = 'video.avi'

# images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# print(len(images))
# print(images)
# frame = cv2.imread(os.path.join(image_folder, images[3]))
# height, width, layers = frame.shape
# print(height, width)
# avgh = 0
# avgw = 0
# for image in images:
#     frame2 = cv2.imread(os.path.join(image_folder, image))
#     height, width, layers = frame2.shape
#     avgh += height
#     avgw += width
    
# no_of_images = len(images)

# mean_w = int(avgw/no_of_images)
# mean_h = int(avgh/no_of_images)

# print(mean_w, mean_h)


# video = cv2.VideoWriter(video_name, 0, 1, (width,height))
# i = 0
# for image in images:
#     if i == 0:
#         i += 1
#         continue
#     else:
#         frame2 = cv2.imread(os.path.join(image_folder, image))
#         height, width, layers = frame2.shape
#         print(height, width, layers)
#         i+=1
#         video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()


# import os
# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw 

# subfolders = [f.path for f in os.scandir("downloads") if f.is_dir() ]    
# # for i in subfolders:
# for f in os.listdir(i):
#     if (ext(f) == '.jpg' or ext2(f) == '.jpeg' or ext3(f) == '.png'):        
#         img = Image.open(os.path.join(i, f))    
#         width, height = img.size
#         print(width, height)
#         basewidth = 1200
#             # print(height)
#         wpercent = (basewidth/float(img.size[0]))
#         hsize = int((float(img.size[1])*float(wpercent)))
#         img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#         new_width, new_height = img.size
#         img.save("newfolder2/{}".format(f))        
#         print(new_width, new_height)
#         print()





# import os 
# import glob
# import shutil

# os.chdir("f:\\xampp\\htdocs\\Python\\NewsReader\\newfolder")


# for i in os.listdir('.'):
#     print(i)


# fnames2 = []
# for files in os.listdir('.'):
#     fnames2.append(files)
# # sort according to time of last modification/creation (os-dependent)
# # reverse: newer files first
# fnames2.sort(key=lambda x: os.stat(x).st_ctime, reverse=False)
# # rename files, choose pattern as you like
# for i, fname in enumerate(fnames2):
#     print(fname + ' : is changed ')    
#     shutil.move(fname, "img-%03d%s" % (i, ".jpg"))




