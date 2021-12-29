import time
import cv2
import os

# Read the video from specified path
video = cv2.VideoCapture("222.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0
print(frame_count)
print(fps)

while (True):
    # reading from frame
    ret, frame = video.read()
    if ret:
        # if video is still left continue creating images
        # fps * 60 yaparsak dakıkada 1 ekran goruntusu
        #alır suankı vıdeo sanıyelık oldugu ıcın sanıyede bır alıyor
        if currentframe%int(fps)==0:
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            # writing the extracted images
            cv2.imwrite(name, frame)


        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
video.release()
cv2.destroyAllWindows()
