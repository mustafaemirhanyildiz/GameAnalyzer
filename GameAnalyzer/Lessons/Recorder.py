from collections import deque
import numpy as np
import cv2
import pyautogui

buffer_size=16
pts=deque(maxlen=buffer_size)

# Red Color
redLower=(0,81,130)
redUpper=(9,252,255)


resolution = pyautogui.size()
codec=cv2.VideoWriter_fourcc(*"XVID")

filename= "Recordin11g.avi"
fps=60.0

out=cv2.VideoWriter(filename,codec,fps,resolution)

cv2.namedWindow("live",cv2.WINDOW_NORMAL)
cv2.resizeWindow("live",480,270)

while True:
    img=pyautogui.screenshot()

    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("live",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

out.release()
