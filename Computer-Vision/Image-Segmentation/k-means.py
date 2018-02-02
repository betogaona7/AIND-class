import numpy as np
import matplotlib.pyplot  as plt 
import cv2 

image = cv2.imread('./../../../images/monarch.jpg')
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Reshape image into a 2D array of pixels and 3 color values (RGB)
pixel_vals = image_copy.reshape((-1,3))

# Convert to float type 
pixel_vals = np.float32(pixel_vals)

# Define stopping criteria 
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Perfom k-means clustering 
k = 2
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert data into 8-bit values
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]

# Reshape data into the original image dimensions 
segmented_image = segmented_data.reshape((image_copy.shape))
labels_reshape = labels.reshape(image_copy.shape[0], image_copy.shape[1])

#plt.imshow(segmented_image)

# Mask image segment
masked_image = np.copy(image_copy)
masked_image[labels_reshape == 1] = [0,0,0]

plt.imshow(masked_image)