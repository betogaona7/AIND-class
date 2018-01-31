import numpy as np 
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('./../../../images/city_hall.jpg')

image_copy = np.copy(image)

# change color to RGB (from BGR)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Convert to grayscale for filtering
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)


# Implement a low-pass filter first
gray_blur = cv2.GaussianBlur(gray, (5,5), 0)

# Create a custom kernel 3x3 to detect vertical edges and ignore 
# horizontal edges
kernel = np.array([[-1, 0, 1],
				   [-2, 0, 2],
				   [-1, 0, 1]])

# Perfom convolution using filter2D which has inputs: (grayscale
# image, bit-depth, kernel)
filtered_image = cv2.filter2D(gray_blur, -1, kernel)
#plt.imshow(filtered_image, cmap='gray')

# Create threshold that sets all the filtered pixels to white 
# above a certain threshold (binary image)

retval, binary_image = cv2.threshold(filtered_image, 100, 255, cv2.THRESH_BINARY)
plt.imshow(filtered_image, cmap='gray')


