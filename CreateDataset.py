#!/usr/bin/env python 
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import sys
import time
import cPickle

video_capture=cv2.VideoCapture(0)
z=0
for i in range (1,65):
	ret,cv_image= video_capture.read()
	cv2.imshow("Image window", cv_image)
	cv2.waitKey(1)
	haar_face_cascade = cv2.CascadeClassifier('/home/paramjit/catkin_ws/src/opencv_ros/src/haarcascade_frontalface_alt.xml')
	test1 = cv_image
	gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
	faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2);
	
	for (x, y, w, h) in faces:
		cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
		crop_img = test1[y:y+h, x:x+w]
		cv2.imshow("cropped", crop_img)
		gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
		
		orb = cv2.ORB_create()
		keyPoints, descriptors = orb.detectAndCompute(gray, None)

		result = cv2.drawKeypoints(crop_img, keyPoints, None, color=(0, 255, 0), flags=0)
		cv2.resize(result, (0,0), fx=0.5, fy=	0.5)
		cv2.imshow('Key points', result)
		dim = (8, 8)
		resized = cv2.resize(result, dim, interpolation = cv2.INTER_AREA)
		cv2.imwrite('1.'+str(z)+'.jpg',resized)
		z=z+1
		cv2.waitKey(1)

	cv2.imshow('Final', test1)
	cv2.waitKey(1)
