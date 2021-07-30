#!/usr/bin/env python
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time 


def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

haar_face_cascade = cv2.CascadeClassifier('/home/paramjit/catkin_ws/src/opencv_ros/src/KeypointDetection/haarcascade_frontalface_alt.xml')

test1 = cv2.imread("/home/paramjit/catkin_ws/src/opencv_ros/src/test1.jpg")
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
cv2.imshow('Test Imag', gray_img)

faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);
print('Faces found: ', len(faces))

for (x, y, w, h) in faces:
	cv2.rectangle(test1, (x, y), (x+w, y+h), (0, 255, 0), 2)
	crop_img = test1[y:y+h, x:x+w]
	cv2.imshow("cropped", crop_img)

cv2.imshow('Text1', test1)




cv2.waitKey(0)
cv2.destroyAllWindows()
