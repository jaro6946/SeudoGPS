import numpy as np
import cv2
from picamera.array import PiRGBArray #https://picamera.readthedocs.io/en/release-1.13/
from picamera import PiCamera
import time



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


def track(src,avgLightColor):
	
	def nothing(*arg):
		pass

	def limit(inputVal,limits):
		output=inputVal
		for i,val in enumerate(inputVal,0):
			if val>limits[i][1]:
				val=limits[i][1]
			elif val<limits[i][0]:
				val=limits[i][0]
			output[i]=val

		return output
	

	img=src.copy()	
	thrs=50
	filt=39
	output=np.zeros(2,len(avgLightColor))

	for j in range(len(avgLightColor)):
		
		upperBound=limit(avgLightColor[i]+thrs/2,[[0,179],[0,255],[0,255]])
		lowerBound=limit(avgLightColor[i]-thrs/2,[[0,179],[0,255],[0,255]])
		mask=np.uint8(cv2.inRange(img,lowerBound,upperBound))


		vis = np.uint8(img.copy())
		vis[mask==0]=(0,0,0)
		
		
		gray2 = img[:,:,2] #only want black and white image
		gray = vis[:,:,2]

		blurred = cv2.GaussianBlur(gray, (filt, filt), 0)

		thresholdValue = cv2.getTrackbarPos('filterThresh', 'image')
		thresh = cv2.threshold(blurred, thresholdValue, 255, cv2.THRESH_BINARY)[1]
		testArray=[(lower-thrs/2).tolist(),(lower+thrs/2).tolist(),lowerBound.tolist(),upperBound.tolist(),thresholdValue]


		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
	

		areas=int(len(cnts))
		splotch = np.zeros((1,areas),dtype=np.uint8)
		
		# loop over the contours
		try:	
			for i,c in enumerate(cnts,0):
			
				M = cv2.moments(c)
				splotch[0][i] = int(M["m00"])
			
			if len(splotch)>0:
				max1=np.argmax(splotch)
			else:
				max1=-1
			
			original=vis.copy()
			
			if max1>0:
				M = cv2.moments(cnts[max1])
				cX = int(M["m10"] / M["m00"])
				cY = int(M["m01"] / M["m00"])
				output[0][j]=cX
				output[1][j]=cY

				
				cv2.drawContours(vis, [cnts[max1]], -1, (0, 255, 0), 2)
				cv2.circle(vis, (cX, cY), 7, (255, 255, 255), -1)
				cv2.putText(vis, i, (cX - 20, cY - 20),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
		except:
			raise
		
		

	visBGR=cv2.cvtColor(vis, cv2.COLOR_HSV2BGR) 
	thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
	
	
	
	ch=cv2.waitKey(1)

	if ch == 27:
		exitNow=True
		break

	return output, vis






