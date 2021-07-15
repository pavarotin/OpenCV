import math
import os
import random

import cv2
import numpy as np
import cv2 as cv




directory = 'temple/'
dict = {}
# for image in os.listdir(directory):
#     img2 = cv.imread(directory+image)
#
#     img3 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#     cv2.imshow('test', img3)
#     cv2.waitKey(0)
#     rt, threshhold = cv.threshold(img3, 150,255,0)
#     contur, hr = cv.findContours(threshhold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#     arr = [contur[1].size, contur[1].min, contur[1].max , 255,0,0]
#     dict[image] = arr

countw = 10
counth = 10

img_rgb = cv.imread('test2.PNG')
width = img_rgb.shape[0]
height = img_rgb.shape[1]
rwidth = width / countw
rheigth = height / counth
img_gray = cv.cvtColor(img_rgb,cv.COLOR_BGR2GRAY)
template1 = cv.imread('temple/empty.PNG')
template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
minefield = np.empty((9,9), dtype="int")
minefield.fill(0)
for pt in zip(*loc[::-1]):
    y =math.trunc (np.absolute( pt[0])  / rwidth)
    x = math.trunc(np.absolute(pt[1]) / rheigth)
    minefield[x][y] = 0

template1 = cv.imread('temple/1.PNG')
template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
minefield = np.empty((9,9), dtype="int")
minefield.fill(0)
for pt in zip(*loc[::-1]):
    y =math.trunc (np.absolute( pt[0])  / rwidth)
    x = math.trunc(np.absolute(pt[1]) / rheigth)
    minefield[x][y] = 1




template1 = cv.imread('temple/2.PNG')
template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    y =math.trunc (np.absolute( pt[0])  / rwidth)
    x = math.trunc(np.absolute(pt[1]) / rheigth)
    minefield[x][y] = 2

template1 = cv.imread('temple/3.PNG')
template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + 10, pt[1] + 10), (128, 128, 10), 1)
    y =math.trunc (np.absolute( pt[0])  / rwidth)
    x = math.trunc(np.absolute(pt[1]) / rheigth)
    minefield[x][y] = 3

template1 = cv.imread('temple/4.PNG')
template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    y =math.trunc (np.absolute( pt[0])  / rwidth)
    x = math.trunc(np.absolute(pt[1]) / rheigth)
    minefield[x][y] = 4


template1 = cv.imread('temple/notPush.PNG')
template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
w = template.shape[0]
h = template.shape[1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    y = math.trunc(np.absolute(pt[0]) / rwidth)
    x = math.trunc(np.absolute(pt[1]) / rheigth)
    minefield[x][y] = 9


print(minefield)
cv.imshow('test',img_rgb)
cv.waitKey(0)
imageMain =  cv2.imread('test.png')
imageMainGray = cv.cvtColor(imageMain,cv.COLOR_BGR2GRAY)
ret2, thresh2 = cv.threshold(imageMainGray, 101,255,0)
contoursMain, hierarchy2 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)




for cnt in contoursMain:
    if cnt.size == dict['1.PNG'][0]:
        cv.drawContours(imageMain, cnt, -1, (random.randint(0,255), random.randint(0,255),random.randint(0,255)), 3)

    elif cnt.size == dict['2.PNG'][0]:
        cv.drawContours(imageMain, cnt, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 3)
    elif cnt.size == dict['empty.PNG'][0]:
        cv.drawContours(imageMain, cnt, -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 3)
        x = 0
        y = 0
        for i in range(0, len(cnt)):
            x, y, w, h = cv2.boundingRect(cnt[i])
        cv.circle(imageMain, (x, y), 10, (0, 0, 255), 5)

cv2.imshow('test',imageMain)
cv2.waitKey(0)