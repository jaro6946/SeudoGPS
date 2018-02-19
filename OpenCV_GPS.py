import GPSfunctions
import numpy as np
import cv2
import time


class timer(object):
	def __init__(self, timerLength):
		self.initTime=time.time()
		self.timerLength=float(timerLength)
	def GO(self):
		self.currentTime=time.time()-self.initTime






while True:
	
	myNumber = str(input("Press RETURN to take initial image"))
	if myResponse is "\n":
		break
	else
		 print("Oops!  That was not return.  Try again...")

initImage=GPSfunctions.image()


while True:
	
	myNumber = str(input("Press RETURN to take comparison image"))
	if myResponse is "\n":
		break
	else
		 print("Oops!  That was not return.  Try again...")

comparisonImage=GPSfunctions.image()

while True:
    try:
         carCount = int(input("How many cars are on the course?"))
         if carCount < 1
         	raise ValueError
         break
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")


diff=compare(initImage, comparisonImage)

cnts = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1][0:carCount]


carCount
contourSize= np.zeros((1,carCount),dtype=np.uint8)
coordinates=[contourSize,contourSize]
avgLightColor=contourSize
# loop over the contours

comparisonImage2=comparisonImage.copy()
for i,c in enumerate(cnts,0):

	lightLocation=np.zeros_like(canvas)
	M = cv2.moments(cnts[i])
	coordinates[0][i]= int(M["m10"] / M["m00"])#x values
	coordinates[1][i] = int(M["m01"] / M["m00"])#y values


	
	cv2.drawContours(lightLocation, [c], -1, 255, -1)

	avgLightColor[i]=mean(comparisonImage,lightLocation)
	print(avgLightColor)


while True:


	if GO is True:
		image=GPSfunctions.image()


		locations, outputImg=GPSfunctions.track(image,avgLightColor)

		cv2.imshow('image',np.hstack([outputImg])) 

	
























