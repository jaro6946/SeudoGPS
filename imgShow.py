


import numpy as np
import cv2
import time


def imgShow(img)

    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image',600,600)

    #make sure the image is facing the right direction
    #img=cv2.flip(img,0)

    #show the image
    cv2.imshow('image',img)

    #waitKey is a function that waits for you to touch a key.  It is required in OpenCV to show images often times.  
    #The 0 in waitkey denotes the function should waith indefinatly for a key stroke.  If you put a number, it will wait for that many milliseconds
    keyStroke=cv2.waitKey(0)

    #If keyStoke in 27 (the ansi key numeral for the esp key) quit from the window
    if keyStroke == 27:
        cv2.destroyAllWindows()
