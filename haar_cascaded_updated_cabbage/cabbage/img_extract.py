import urllib.request
import cv2
import numpy as numpy
import os
import socket
socket.setdefaulttimeout(30)

def store_raw_image():
    cabbage_image_link = open('cabbage.txt','r')
    cabbage_image_urls = cabbage_image_link.readlines()

    if not os.path.exists('cabbage'):
        os.makedirs('cabbage')
    pic_num = 1

    for i in cabbage_image_urls:
        try:
            print(str(pic_num) + ': '+str(i))
            urllib.request.urlretrieve(i, "cabbage/" + str(pic_num) + '.jpg')
            img = cv2.imread("cabbage/" + str(pic_num) + '.jpg')
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("cabbage/" + str(pic_num) + '.jpg', resized_image)
            pic_num += 1
       
        except Exception as e:
            print(str(e))


store_raw_image()