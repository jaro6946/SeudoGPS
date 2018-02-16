import GPSfunctions
import numpy as np
import cv2
import time


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



diff = cv2.absdiff(initImage, comparisonImage)
mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

th = 1
imask =  mask>th

canvas = np.zeros_like(img2, np.uint8)
canvas[imask] = img2[imask]


cnts = cv2.findContours(imask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1][0:carCount]


carCount
contourSize= np.zeros((1,carCount),dtype=np.uint8)
coordinates=[contourSize,contourSize]
# loop over the contours

for i,c in enumerate(cnts,0):

	M = cv2.moments(cnts[i])
	coordinates[0][i]= int(M["m10"] / M["m00"])
	coordinates[1][i] = int(M["m01"] / M["m00"])


	
	cv2.drawContours(vis, [c], -1, (0, 255, 0), 2)
	cv2.circle(vis, (cX, cY), 7, (255, 255, 255), -1)
	
	cv2.putText(vis, i, (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)






























