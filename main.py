import cv2
import numpy as np
import cv2 as cv


image = cv2.imread('temple/1.PNG')
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 101, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

imageMain =  cv2.imread('test.png')
imageMainGray = cv.cvtColor(imageMain,cv.COLOR_BGR2GRAY)
ret2, thresh2 = cv.threshold(imageMainGray, 101,255,0)
contoursMain, hierarchy2 = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
lenOne = contours[1].size

print(lenOne)

for cnt in contoursMain:
    if cnt.size == lenOne:
        cv.drawContours(imageMain, cnt, -1, (0, 255, 0), 3)


cv2.imshow('test',imageMain)
cv2.waitKey(0)