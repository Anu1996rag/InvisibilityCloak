# importing the libraries

import cv2
import numpy as np
import time

print("Get ready to disappear...")

# capturing the video
capture = cv2.VideoCapture(0) #here , 0 means we are using the web cam

#let the camera record the backgroud image for the first 3 seconds
time.sleep(3)

#capturing the background
background = 0

for i in range(30):
    ret, background = capture.read()

#actual logic
# while the camera is open
while(capture.isOpened()):
    ret, img = capture.read()

    if not ret:
        break
    #converting the image into the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #defining the lower range for the red color detection
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    #defining the lower range for the red color detection
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    #Adding the two masks to generate the final mask
    mask = mask1 + mask2

    #performing the noise removal from the image
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    #Replacing the cloak image pixels with the background pixels
    img[np.where(mask==255)] = background[np.where(mask==255)]

    cv2.imshow('Reveal',img)

    #to stop the execution of the program whenever we use the ESC key
    k = cv2.waitKey(10)
    if k == 27:
        break

#closing all the windows and camera
capture.release()
cv2.destroyAllWindows()