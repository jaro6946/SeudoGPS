import numpy as np
import cv2
import sys
from picamera.array import PiRGBArray #https://picamera.readthedocs.io/en/release-1.13/
#This sintax (from ... import...) only imports a single class/fuction from the module.  PiRGB in this case.
from picamera import PiCamera
import time



def image()
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)
 
# grab an image from the camera 
camera.capture(rawCapture, format="bgr")
img = rawCapture.array


#make sure the image is facing the right direction
#img=cv2.flip(img,0)

return img


