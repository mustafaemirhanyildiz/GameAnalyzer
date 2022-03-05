import pytesseract
from PIL import Image
import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img=cv2.imread("../Images/Csgo6.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=img[0:400,1000:]
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
words_in_image = pytesseract.image_to_string(img)
print(words_in_image)
plt.show()

_,thresh_img=cv2.threshold(img,thresh=150,maxval=255,type=cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.axis("off")
words_in_image = pytesseract.image_to_string(thresh_img)
print(words_in_image)
plt.show()


#adaptive thresh holding

thresh_img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)