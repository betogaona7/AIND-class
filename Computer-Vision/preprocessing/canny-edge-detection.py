import numpy as np
import matplotlib.pyplot as plt 
import cv2

image = cv2.imread('./../../../images/flower.jpg')

image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

# Define lower and upper thresholds for hysteresis 
lower = 180
upper = 240

# implement canny edge detection
egdes = cv2.Canny(gray, lower, upper)
plt.imshow(edges, cmap='gray')
