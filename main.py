import os
import random

import cv2
import numpy as np
import cv2 as cv




directory = 'temple/'
dict = {}
for image in os.listdir(directory):
    img2 = cv.imread(directory+image)
    cv2.imshow('test', img2)
    cv2.waitKey(0)
    img3 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    rt, threshhold = cv.threshold(img3, 101,255,0)
    contur, hr = cv.findContours(threshhold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    arr = [contur[1].size, contur[1].min, contur[1].max , 255,0,0]
    dict[image] = arr

imageMain =  cv2.imread('test.png')
imageMainGray = cv.cvtColor(imageMain,cv.COLOR_BGR2GRAY)
ret2, thresh2 = cv.threshold(imageMainGray, 101,255,0)
contoursMain, hierarchy2 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)




for cnt in contoursMain:
    if cnt.size == dict['1.PNG'][0]:
        cv.drawContours(imageMain, cnt, -1, (random.randint(0,255), random.randint(0,255),random.randint(0,255)), 3)

        for i in range(0, len(cnt)):
            x, y, w, h = cv2.boundingRect(cnt[i])
            print(x)
    elif cnt.size == dict['2.PNG'][0]:
        cv.drawContours(imageMain, cnt, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 3)


cv2.imshow('test',imageMain)
cv2.waitKey(0)