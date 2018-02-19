
import cv2
import sys
from imgShow import imgShow
import numpy as np

def compare(initImage, comparisonImage):
	diff = cv2.absdiff(initImage, comparisonImage)
	diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

	return diff

if __name__=="__main__" :
	baselineImg=cv2.imread(sys.argv[1])
	lightsOnImg=cv2.imread(sys.argv[2])

	resultImg=compare(baselineImg,lightsOnImg)
	resultImg=cv2.cvtColor(resultImg, cv2.COLOR_GRAY2BGR)
	imgShow(np.hstack([baselineImg,lightsOnImg,resultImg]))
