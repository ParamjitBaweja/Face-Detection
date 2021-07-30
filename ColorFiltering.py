#!/usr/bin/env python
import numpy as np
import cv2 
#import imutils

image_name="cones"

print("reading image from file")
img=cv2.imread("<path>/cones.jpg")
print(img)
cv2.imshow("rgbimage",img)

print("hsv")
hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv)
cv2.imshow("hsvimage",hsv)

print("mask")
yellowLower=(35,0,0)
yellowUpper=(50,255,255)
blueLower=(120,0,0)
blueUpper=(150,255,255)
mask1 = cv2.inRange(hsv,yellowLower,yellowUpper)
mask2 = cv2.inRange(hsv,blueLower,blueUpper)
mask = cv2.bitwise_or(mask1, mask2)
cv2.imshow("mask",mask)

print("final")
target = cv2.bitwise_and(hsv,hsv, mask=mask)
cv2.imshow("final",target)

cv2.waitKey(0)
cv2.destroyAllWindows()


