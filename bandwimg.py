import numpy as np
import cv2
from PIL import Image
from scipy.misc import imsave
import turtle
import sys
wn = turtle.Screen()
wn.bgcolor("black")
turtle.ht()
turtle.hideturtle()
turtle.speed(0)

def draw(x,y):
    
    skip = 0
    for i,j in zip(x,y):
        if skip%8 == 0 :
            turtle.goto(i,j)
            turtle.dot('blue')
        skip += 1
   
     



def black_and_white(img_path):

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,(400,400))
    img = np.array(img)

    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] < 150:
                img[i][j] = 0

            else:
                img[i][j] = 255
    
    imsave('n.jpg',img)
    return img

def coordinates(img):
    co = []
    ch = -1
    black_pixel = np.array(np.where(img == 0))
    print(black_pixel.ndim,black_pixel.shape,len(black_pixel))
    return black_pixel


if len(sys.argv) < 2:
    print("Please provide full name of the image as argument.")

else:
    for img in sys.argv[1:]:
        img = black_and_white(img)
        print("done")
        co = coordinates(img)
        draw(co[0],co[1])
