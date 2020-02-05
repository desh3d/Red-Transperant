import cv2, time
import numpy as np
############  MAKE RED INVISIBLE  ##############
#### THIS PROGRAM CAN SEE THROUGH RED COLOR  ########
cap = cv2.VideoCapture(0)     # 0 for truning on laptop camera and start recording
time.sleep(3)
background = 0
for i in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)


while(cap.isOpened()):
    ret, img = cap.read() # gets the first background image
    img = np.flip(img, axis=1) # flips the image array, understand it throughly
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # cv cannot see rgb as we do, so convert each to hsv
    value = (35,35)   # one pixel size
    blured = cv2.GaussianBlur(hsv, value,0) # blurs the hsv image
    lower_red = np.array([0,100,30]) # put 0,100,30 for yellow
    upper_red = np.array([60,255,255]) # put 60,255,255 for yellow
    mask1 = cv2.inRange(hsv,lower_red,upper_red) # old image color range apply on hsv
    
    
    lower_red = np.array([125,100,30]) # put 125,100,30 for yellow
    upper_red = np.array([255,255,255])## put 255,255,255 for yello
    mask2 = cv2.inRange(hsv, lower_red,upper_red) # new image color range apply on hsv
    mask = mask1+mask2  # total color range
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN, np.ones((5,5),np.uint8))# make old image overlap with new image at pixels of size 35,35
    img[np.where(mask==255)] = background[np.where(mask==255)] # combine masks
    cv2.imshow('Display',img) #show
    k= cv2.waitKey(10) #scans which key was pressd in last 10 milliseconds
    if k == 27:  # Press ESCAPE TO EXIT
        break
    
cap.release()    ## run in compiler to close camera
cv2.destroyAllWindows() 
  
"""
lower_red=np.array([0,120,70])  # put 0,100,30 for yellow
    upper_red=np.array([10,255,255]) # put 60,255,255 for yellow
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    lower_red=np.array([170,120,70]) # put 125,100,30 for yellow
    upper_red=np.array([180,255,255]) # put 255,255,255 for yellow
"""

cap.release()










