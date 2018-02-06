
"""
 Code notes of class
"""

"""----- GRADIENT MAGNITUDE AND DIRECTION -----"""

# Read in your image and convert to grayscale
image = cv2.imread('car1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Compute the gradients in the x and y directions
gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1)

# Compute the magnitude and direction of the image gradient
mag, ang = cv2.cartToPolar(gx, gy)

"""----- DEFINE THE CELLS AND BINS -----"""

# Creating bin ranges
n_bins = 9
bins = np.int32(n_bins*ang/(2*np.pi))

"""----- CALCULATE THE HISTOGRAM FOR EACH CELL -----"""

# Parameters you define for a HOG feature vector
win_size = (64, 64)
block_size = (16, 16)
block_stride = (5, 5)
cell_size = (8, 8)
n_bins = 9

# Create the HOG descriptor
hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, n_bins)

# Using the descriptor, calculate the feature vector of an image
feature_vector = hog.compute(image)

#The feature vector that this produces is what you can use to train a classifier!

"""----- SVM -----"""

# Define the SVM training parameters
svm_params = dict( kernel_type = cv2.SVM_LINEAR,
                    svm_type = cv2.SVM_C_SVC,
                    C=2.67, gamma=5.383 )

# Initialize the SVM
svm = cv2.SVM()

"""----- TRAINING -----"""

# Read in sets of images and their labels
all_images = glob.glob('*.jpeg')
labels = glob.glob('*.txt')

# Form your HOG training data
hog_data = [map(hog, labels) for image in all_images]
training_data = np.float32(hog_data)

# Train and save your SVM
svm.train(trainData, labels, params=svm_params)
svm.save('svm_model.dat')

"""----- TESTING -----"""

# After reading in the test data and determining the HOG feature vectors
test_data = np.float32(test_hog_data)

# Test the SVM model
result = svm.predict_all(test_data)

# Check the accuracy
mask = result==labels
correct = np.count_nonzero(mask)
print (correct*100.0/result.size)