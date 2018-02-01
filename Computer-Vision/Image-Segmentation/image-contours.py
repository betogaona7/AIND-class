import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('./../../../images/hands.jpg')
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Convert to grayscale 
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

# Create a binary thresholded image
retval, binary = cv2.threshold(gray, 225, 255, cv2.TRESH_BINARY_INV)
#plt.imshow(binary, cmap='gray')

# Find contours from threshold image 
retval, contours, hierachy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the first contour (index = 0)
#selected_contour = contours[0]
#contour_image = cv2.drawContours(contour_image, [selected_contour], 0, (0,255,0), 3)

# Draw all countours on a copy of the original image
image_copy2 = np.copy(image_copy)
all_contours = cv2.drawContours(image_copy2, contours, -1, (0,255,0), 2)
plt.imshow(all_contours)

def orientation(contours):
	angles = []
	for contour in contours:
		# Fit an ellipse to a contour to extract the angle from that ellipse
		(x,y), (MA, ma), angle = cv2.fitEllipse(contour)
		angles.append(angle)
	return angles

def crop(image, selected_contour):
	cropped_image = np.copy(image)
	# Find the bounding rectangle of a selected contour 
	x, y, w, h = cv2.boundingRect(selected_contour)
	# Draw the bounding rectangles as a purple box 
	#cropped_image = cv2.rectangle(image, (x,y), (x+w,y+h), (200,0,200),2)
	# Crop using the dimensions of the bounding rectangle
	cropped_image = image[y: y+h, x: x+w]
	return cropped_image
