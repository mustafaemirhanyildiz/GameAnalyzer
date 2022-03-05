import cv2
import numpy as np
from cvzone import stackImages



def empty(a):
    pass
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",200,255,empty)
cv2.createTrackbar("Threshold2","Parameters",255,255,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)

def getContours(img,imgContour):

    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        areaMin=cv2.getTrackbarPos("Area","Parameters")
        peri=cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,0.02*peri,True)
        if len(approx)==4 and area>2500:

            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            """x,y,w,h=cv2.boundingRect(approx)

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)

            cv2.putText(imgContour,"Points:",str(len(approx)),
                        (x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
            cv2.putText(imgContour,"Area:",str(int(approx)),
                        (x+w+20,y+45),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)"""



while True:
    img=cv2.imread("../Images/Valorant.png") #read image

    imgContour=img.copy()

    imgBlur=cv2.GaussianBlur(img,(7,7),1)

    imgGray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    threshold1=cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2=cv2.getTrackbarPos("Threshold2","Parameters")

    imgCanny=cv2.Canny(imgGray,threshold1,threshold2)

    kernel=np.ones((5,5))
    imgDil=cv2.dilate(imgCanny,kernel,iterations=1)

    getContours(imgDil,imgContour)

    imgStack=stackImages(([img,imgGray,imgCanny,imgDil,imgContour,imgContour]),3,0.3)


    cv2.imshow("Original->Gray->Canny->Dialation->getContours->getContours",imgStack)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break