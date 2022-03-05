import cv2
import numpy as np
from collections import deque
from cvzone import ColorFinder

buffer_size=16
pts=deque(maxlen=buffer_size)

# Red Color
redLower=(0,81,130)
redUpper=(9,252,255)
whiteLower=(0,0,180)
whiteUpper=(25,42,255)
#capture

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,960)



while True:
    imgOriginal = cv2.imread("../Images/CsgoImage2.jpg")

    #blur
    blurred=cv2.GaussianBlur(imgOriginal,(11,11),0)

    #hsv
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    cv2.imshow("Hsv Image",hsv)

    # mask for red
    maskRed=cv2.inRange(hsv,redLower,redUpper)
    cv2.imshow("Mask Image Red",maskRed)
    maskWhite=cv2.inRange(hsv,whiteLower,whiteUpper)
    cv2.imshow("Mask Image White",maskWhite)



    #contours
    contoursRed,_=cv2.findContours(maskRed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contoursWhite,_=cv2.findContours(maskWhite.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


    center = None

    if len(contoursRed)>0 and len(contoursWhite)>0:
        #get the biggest contour
        c=max(contoursRed,key=cv2.contourArea)

        #rectangular
        rect=cv2.minAreaRect(c)

        ((x,y),(width,height),(rotation))=rect

        s="x: {} , y: {}, width= {},height= {},rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))


        #box

        box=cv2.boxPoints(rect)
        box=np.int64(box)

        #moment
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))

        #draw contour
        cv2.drawContours(imgOriginal,[box],0,(0,255,255),2)

        cv2.circle(imgOriginal,center,5,(255,0,255),-1)

        cv2.putText(imgOriginal,s,(250,250),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)

    cv2.imshow("original tespit",imgOriginal)



    if cv2.waitKey(1) & 0xFF== ord("q"):
        break


