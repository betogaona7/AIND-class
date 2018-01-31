import numpy as np
import matplotlib.pyplot as plt
import cv2


image = cv2.imread('./../../../images/skewed_bussiness_card.jpg')

# Make a copy of the image and change color to RGB (from BGR)
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
#plt.imshow(image_copy)

# Find and select four points in source image (X, Y)
"""
plt.plot(60, 360, '.') # Top left corner
plt.plot(290, 645, '.') # Bottom left
plt.plot(760, 175, '.') # Bottom right
plt.plot(515, 100, '.') # Top right
"""

def warp(image):
	# Four source coordinates, which define a rectangular plane
	source_pts = np.float32(
		[[60, 360],
		[290, 645],
		[760, 175],
		[515, 100]])

	# Four warped coordinates 
	warped_pts = np.float32(
		[[100, 200],
		 [100, 550],
		 [800, 550],
		 [800, 200]])

	# Compute the perspective transform
	M = cv2.getPerspectiveTransform(source_pts, warped_pts)

	# Get the image size and compute and return the warped image
	image_size = (image.shape[1], image.shape[0])
	warped = cv2.warpPerspective(image, M, image_size, flags=cv2.INTER_LINEAR)
	return warped

warped_image = warp(image_copy)

# Create a side by side plots 
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

ax1.set_title('Source image')
ax1.imshow(image_copy)

ax2.set_title('Warped image')
ax2.imshow(warped_image)
