import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('./../../../images/phone.jpg')
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Convert image to grayscale
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

# Define out parameters for Canny
low_threshold = 50
high_threshold = 100
edges = cv2.Canny(gray, low_threshold, high_threshold)

# Define the Hough transform parameters 
rho = 1
theta = np.pi/180
threshold = 60
min_line_length = 100
max_line_gap = 5

# Find lines using a Hough transform 
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
line_image = np.copy(image_copy)

# Iterate over the output lines and draw lines on the image copy
for line in lines:
	for x1, y1, x2, y2 in line:
		cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 5)
plt.imshow(line_image)