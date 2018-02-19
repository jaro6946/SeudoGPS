

import sys
from imgShow import imgShow

def compare(baselineImg, lightsOnImg)
	diff = cv2.absdiff(initImage, comparisonImage)
	diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

	return diff

if "__main__ " == __name__
	
	print(sys.argv[0])

	#resultImg=compare(baselineImg,lightsOnImg)
	#imgShow(resultImg)