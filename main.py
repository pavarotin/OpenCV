import math
import os
import random
import  time
import win32api, win32con
import cv2
import numpy as np
import cv2 as cv

import pyautogui as pag
def leftClickOn(i, y):
    win32api.SetCursorPos((644 + (y * 60), 287 + (i * 60),))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.001)
   # pag.click(button='left')


def rightClickOn(i, y):
    #pag.moveTo(, speedMouse)
    win32api.SetCursorPos((644 + (y * 60), 287 + (i * 60),))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
    #pag.click(  button='Right')

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __hash__(self):

        return hash((self.x, self.y))

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y
def setFlag():

    countNeigb = 0
    coordNeigb = set([])
    for i in range(9):
        for y in range(9):
            if minefield[i, y] in range(1, 6):
                countNeigb = 0
                coordNeigb.clear()
                if  i!=0 and minefield[i - 1, y]  == 9 or i!=0 and minefield[i - 1, y] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i-1, y))

                if y != 0 and minefield[i, y - 1] == 9 or y != 0 and minefield[i, y - 1] ==  -1 :
                    countNeigb += 1
                    coordNeigb.add(Point(i, y-1))
                if  i != 8 and minefield[i + 1, y] == 9 or  i != 8 and minefield[i + 1, y] ==  -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i+1, y))
                if y != 8 and minefield[i, y + 1] == 9 or y != 8 and  minefield[i, y + 1] ==-1:
                    countNeigb += 1
                    coordNeigb.add(Point(i, y+1))
                if y != 0 and i !=0 and minefield[i - 1, y - 1] == 9 or minefield[i - 1, y - 1] ==  -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i-1, y-1))
                if i!=0 and y != 8 and minefield[i - 1, y + 1] == 9 or i!=0 and y != 8 and minefield[i - 1, y + 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i-1, y+1))
                if i != 8 and y != 8 and minefield[i + 1, y + 1] == 9 or i != 8 and y != 8 and minefield[i + 1, y + 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i+1, y+1))
                if i != 8 and y != 0 and minefield[i + 1, y - 1] == 9 or i != 8 and y != 0 and minefield[i + 1, y - 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i+1, y-1))


            if minefield[i, y] == countNeigb:
                for c in coordNeigb:

                    if minefield[c.x,c.y] != -1:
                        rightClickOn(c.x, c.y)

                        minefield[c.x, c.y] = -1


def countNotPush(i,y):
        countNeigb = 0
        if  i != 0 and minefield[i - 1, y] == 9:
            countNeigb += 1
        if  y != 0 and minefield[i, y - 1] == 9:
            countNeigb += 1
        if  i != 8 and minefield[i + 1, y] == 9:
            countNeigb += 1
        if  y != 8 and minefield[i, y + 1] == 9:
            countNeigb += 1
        if y != 0 and i != 0 and minefield[i - 1, y - 1] == 9 :
            countNeigb += 1
        if i != 0 and y != 8 and minefield[i - 1, y + 1] == 9:
            countNeigb += 1
        if i != 8 and y != 8 and minefield[i + 1, y + 1] == 9:
            countNeigb += 1
        if i != 8 and y != 0 and minefield[i + 1, y - 1] == 9:
            countNeigb += 1

        return  countNeigb

def deFLag():

    countNeigb = 0
    coordNeigb = set([])
    for i in range(9):
        for y in range(9):
            if minefield[i, y] in range(1, 6):
                countNeigb = 0
                coordNeigb.clear()
                if  i != 0 and minefield[i - 1, y] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i - 1, y))

                if  y != 0 and minefield[i, y - 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i, y - 1))
                if  i != 8 and minefield[i + 1, y] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i + 1, y))
                if  y != 8 and minefield[i, y + 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i, y + 1))
                if y != 0 and i != 0 and minefield[i - 1, y - 1] == -1 :
                    countNeigb += 1
                    coordNeigb.add(Point(i - 1, y - 1))
                if i != 0 and y != 8 and minefield[i - 1, y + 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i - 1, y + 1))
                if i != 8 and y != 8 and minefield[i + 1, y + 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i + 1, y + 1))
                if i != 8 and y != 0 and minefield[i + 1, y - 1] == -1:
                    countNeigb += 1
                    coordNeigb.add(Point(i + 1, y - 1))
            # for isa in coordNeigb:
            #     if coordNeigb.count(isa) > 1:
            #         coordNeigb.remove(isa)

            if countNotPush(i,y) != 0:
                if minefield[i,y] in range(1,6) and  minefield[i, y] == countNeigb :
                    leftClickOn(i , y)



               # print({minefield[c.y, c.x]}, " Leftclick x:y", {c.x}, ":", {c.y})
               #  if i != 0 and Point( i - 1, y) not in coordNeigb and minefield[i-1,y] ==9:
               #      leftClickOn(i-1,y)
               #
               #  if y != 0 and minefield[i, y - 1] not in coordNeigb and minefield[i,y-1] ==9:
               #      leftClickOn(i,y-1)
               #  if i != 8 and minefield[i + 1, y] not in coordNeigb and minefield[i+1,y] ==9:
               #      leftClickOn(i+1,y)
               #  if y != 8 and minefield[i, y + 1] not in coordNeigb and minefield[i,y+1] ==9:
               #      leftClickOn(i , y+1)
               #  if y != 8 and i != 8 and minefield[i - 1, y - 1] not in coordNeigb and minefield[i-1,y-1] ==9:
               #      leftClickOn(i-1,y-1)
               #  if i != 0 and y != 8 and minefield[i - 1, y + 1] not in coordNeigb and minefield[i-1,y+1] ==9:
               #      leftClickOn(i-1,y+1)
               #  if i != 8 and y != 8 and minefield[i + 1, y + 1] not in coordNeigb and minefield[i+1,y+1] ==9:
               #      leftClickOn(i+1,y+1)
               #  if i != 8 and y != 0 and minefield[i + 1, y - 1] not in coordNeigb and minefield[i+1,y-1] ==9:
               #      leftClickOn(i+1,y-1)


while True:
    # cv2.imshow('test', cv.imread('test2.PNG'))
    # cv2.waitKey(0)
    pag.screenshot('gus.png',region=(608, 248, 570, 570))
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
    img_rgb = cv.imread('gus.PNG')
    width = img_rgb.shape[0]
    height = img_rgb.shape[1]
    rwidth = width / countw
    rheigth = height / counth
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    template1 = cv.imread('temple/1.PNG')
    template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    minefield = np.empty((9, 9), dtype="int")
    minefield.fill(0)
    for pt in zip(*loc[::-1]):
        y = math.trunc(np.absolute(pt[0]) / rwidth)
        x = math.trunc(np.absolute(pt[1]) / rheigth)
        minefield[x][y] = 1

    template1 = cv.imread('temple/2.PNG')
    template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        y = math.trunc(np.absolute(pt[0]) / rwidth)
        x = math.trunc(np.absolute(pt[1]) / rheigth)
        minefield[x][y] = 2
    #leftClickOn(0,0)
    template1 = cv.imread('temple/3.PNG')
    template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + 10, pt[1] + 10), (128, 128, 10), 1)
        y = math.trunc(np.absolute(pt[0]) / rwidth)
        x = math.trunc(np.absolute(pt[1]) / rheigth)
        minefield[x][y] = 3

    template1 = cv.imread('temple/4.PNG')
    template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        y = math.trunc(np.absolute(pt[0]) / rwidth)
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

    template1 = cv.imread('temple/flag.PNG')
    template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        y = math.trunc(np.absolute(pt[0]) / rwidth)
        x = math.trunc(np.absolute(pt[1]) / rheigth)
        minefield[x][y] = -1
    #pag.screenshot('win.png', region=(827, 104, 120, 120))
    # template1 = cv.imread('temple/die.PNG')
    # template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
    # img_gray = cv.cvtColor(cv.imread('win.PNG'), cv.COLOR_BGR2GRAY)
    # res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # threshold = 0.9
    # if len(loc[0]) > 1 and loc[0][0] is not None:
    #     pag.click((827,104), button='Left')
    #     continue
    #
    # pag.screenshot('win.png', region=(827, 104, 120, 120))
    # template1 = cv.imread('temple/finish.PNG')
    # template = cv.cvtColor(template1, cv.COLOR_BGR2GRAY)
    # img_gray = cv.cvtColor(cv.imread('win.PNG'), cv.COLOR_BGR2GRAY)
    # res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # threshold = 0.9
    # if len(loc[0]) > 1 and loc[0][0] is not None:
    #     pag.click((827, 104), button='Left')
    #     continue


    # cv.imshow('test', img_rgb)
    # cv.waitKey(0)
   # imageMain = cv2.imread('test.png')

    scrW, scrH = pag.size()

    speedMouse = 0.1


    if(np.sum(minefield) > 728):
        continue




    setFlag()

    deFLag()
    #markFlag()
    # cv2.imshow('test', imageMain)
    # cv2.waitKey(0)


