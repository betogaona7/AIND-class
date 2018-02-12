import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('./../../../images/skewed_chesboard.png')
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

# Convert to float type
gray = np.float32(gray)

# Detect corners 
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate corner image to enhance corner points 
dst = cv2.dilate(dst, None)

#plt.imshow(dst, cmap='gray')

# Define a threshold for extracting strong corners 
# this value may vary depending on the image
thresh = 0.01*dst.max()

# Create an umage copy to draw corners on
corner_image = np.copy(image_copy)

# Iterate through all the corners and draw them on the image (if they pass the threshold)
for i in range(0, dst.shape[0]):
	for j in range(0, dst.shape[1]):
		if(dst[i,j] > thresh):
			# Image, center pt, radius, color, thickness
			cv2.circle(corner_image, (j,i), 2, (0,255,0), 1)
plt.imshow(corner_image)

def dilation(image):
	binary_image = cv2.imread(image, 0)
	# Create a 5x5 kernel of ones
	kernel = np.ones((5,5), np.unit8)
	# Dilate the image
	dilate_image = cv2.dilate(binary_image, kernel, iterations=1)
	return dilate_image

def erosion(image):
	binary_image = cv2.imread(image, 0)
	# Create a 5x5 kernel of ones
	kernel = np.ones((5,5), np.unit8)
	# Dilate the image
	erode_image = cv2.erode(binary_image, kernel, iterations=1)
	return erode_image