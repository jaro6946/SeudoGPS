import GPSfunctions
import numpy as np
import cv2
import time
import sys


if len(sys.argv)>2
	initImage=cv2.imread(sys.argv[1])
	comparisonImage=cv2.imread(sys.argv[2])

else:

	while True:
		
		myNumber = str(input("Press RETURN to take initial image"))
		if myResponse == "\n":
			break
		else
			 print("Oops!  That was not return.  Try again...")

	initImage=GPSfunctions.image()


	while True:
		
		myNumber = str(input("Press RETURN to take comparison image"))
		if myResponse == "\n":
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

cnts = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
if len(cnts)>carCount
	cnts=cnts[0:carCount]
elif len(cnts < carCount)
	print('{0} out of {1} cars were found'.format(len(cnts),carCount))


contourSize= np.zeros((1,carCount),dtype=np.uint8)
coordinates=np.zeros((2,carCount),dtype=np.uint16)
avgLightColor=contourSize
# loop over the contours

comparisonImage2=comparisonImage.copy()


for i,c in enumerate(cnts,0):

	lightLocation=np.zeros_like(initImage)
	M = cv2.moments(c)
	coordinates[0][i]= int(M["m10"] / M["m00"])#x values
	coordinates[1][i] = int(M["m01"] / M["m00"])#y values


	
	cv2.drawContours(lightLocation, [c], -1, 255, -1)

	avgLightColor[i]=mean(comparisonImage,lightLocation)
	print(avgLightColor)

timer1=GPSfunctions.timer(3)


while True:


	if timer1.GO is True:
		
		image=GPSfunctions.image()


		locations, outputImg=GPSfunctions.track(image,avgLightColor)

		cv2.imshow('image',np.hstack([outputImg])) 

	
























