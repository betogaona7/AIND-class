from matplotlib import pyplot as plt
import numpy as np
import cv2

# Read the image 
image = cv2.imread('./images/pizza_bluescreen.jpg')

print('This image is: ', type(image), ' with dimensions: ', image.shape)
#plt.imshow(image)

# Make a copy of the image and change color to RGB (from BGR)
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
#plt.imshow(image_copy)

# Define our color selection boundaries in RGB values
lower_blue = np.array([0, 0, 220])
upper_blue = np.array([50,70,255])

# Create a masked area
mask = cv2.inRange(image_copy, lower_blue, upper_blue)
#plt.imshow(mask, cmap='gray')

# Mask the image to let the object show through
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
plt.imshow(masked_image)

# Load in a background image, and convert it to RGB
background_image = cv2.imread('./images/space_background.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

# Crop it to the right size
crop_background = background_image[0:720, 0:1280]

# Mask the cropped background
crop_background[mask == 0] = [0, 0, 0]
#plt.imshow(crop_background)

# Add the two images together to create a complete image
complete_image = crop_background + masked_image
#plt.imshow(complete_image)

cv2.imwrite('./images/completeimg.jpg', cv2.cvtColor(complete_image, cv2.COLOR_BGR2RGB))
