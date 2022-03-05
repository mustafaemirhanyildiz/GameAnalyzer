import cv2  # pip install opencv-python
import os
from os.path import isfile, join
import numpy as np


def convert_pictures_to_video(pathIn, pathOut, fps, time):
    redLower = (0, 81, 130)
    redUpper = (9, 252, 255)
    whiteLower = (0, 0, 180)
    whiteUpper = (25, 42, 255)
    ''' this function converts images to video'''
    frame_array=[]
    files=[f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]
    for i in range (len(files)):
        filename=pathIn+files[i]
        '''reading images'''
        img=cv2.imread(filename)
        blurred = cv2.GaussianBlur(img, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        maskRed = cv2.inRange(hsv, redLower, redUpper)
        maskWhite = cv2.inRange(hsv, whiteLower, whiteUpper)
        contoursRed, _ = cv2.findContours(maskRed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contoursWhite, _ = cv2.findContours(maskWhite.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        enter = None

        if len(contoursRed) > 0 and len(contoursWhite) > 0:
            # get the biggest contour
            c = max(contoursRed, key=cv2.contourArea)

            # rectangular
            rect = cv2.minAreaRect(c)

            ((x, y), (width, height), (rotation)) = rect

            s = "x: {} , y: {}, width= {},height= {},rotation: {}".format(np.round(x), np.round(y), np.round(width),
                                                                          np.round(height), np.round(rotation))

            # box

            box = cv2.boxPoints(rect)
            box = np.int64(box)

            # moment
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # draw contour
            cv2.drawContours(img, [box], 0, (0, 255, 255), 2)

            cv2.circle(img, center, 5, (255, 0, 255), -1)

            cv2.putText(img, s, (250, 250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)

        # img=cv2.resize(img,(1400,1000))
        height, width, layers = img.shape
        size=(width,height)


        for k in range (time):
            frame_array.append(img)
    out=cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps,size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

# Example:
directory= r'C:\Users\Musta\PycharmProjects\OpencvCourse\Images'
pathIn=directory+'/'
pathOut=pathIn+'video_EX9.avi'
fps=1
time=20 # the duration of each picture in the video
convert_pictures_to_video(pathIn, pathOut, fps, time)