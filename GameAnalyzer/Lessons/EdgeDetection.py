import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("../Images/Musty.jpg", 0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off")
