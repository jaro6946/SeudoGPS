import numpy as np
import cv2
from picamera.array import PiRGBArray #https://picamera.readthedocs.io/en/release-1.13/
from picamera import PiCamera
import time
from math import floor



def image():
	camera = PiCamera()
	rawCapture = PiRGBArray(camera)
	 
	# allow the camera to warmup
	time.sleep(0.1)
	 
	# grab an image from the camera 
	camera.capture(rawCapture, format="bgr")
	img = rawCapture.array
	img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	#make sure the image is facing the right direction
	#img=cv2.flip(img,0)

	return img

def sigDig(num):
	num1=str(float(num))
	digitsRightDecimal=-len(num1.split('.')[1])
	for i,val in enumerate(num1[::-1],digitsRightDecimal):

		if val != '0' and val != '.':
			if i > 0:
				i=i-1 

			return -i
	raise ValueError 


class timer(object):
	def __init__(self, timerLength):
		self.initTime=time.time()
		self.timerLength=float(timerLength)
		self.sigDigits=sigDig(self.timerLength)
		self.flag=0
		
	def GO(self):
		self.currentTime=time.time()-self.initTime
		self.roundedTime=round(self.currentTime,self.sigDigits)
		self.ratio=(self.currentTime/self.timerLength)-floor(self.currentTime/self.timerLength)
		if self.ratio < .99:
			if self.flag==1:
				self.flag=0
			return False
		elif self.flag==0:
			self.flag=1
			return True
if __name__=="__main__":
	time1=timer(.5)

	while True:
		if time1.GO() == True:
			print(time1.currentTime)
			










