import subprocess as ss
import time
from cv2 import *

ramp_frames=50



def capture():
	cam = VideoCapture(0)   # 0 -> index of camera	
	for i in xrange(ramp_frames):	#making image quality better
		temp = cam.read()
	
	s,img=cam.read()
	
	if s:    # frame captured without any errors
	    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
#	    imshow("cam-test",img)
#	    waitKey()
	    imwrite("captured_image.jpg",img) #save image


def main():
	capture()


if __name__=="__main__":
	main()


