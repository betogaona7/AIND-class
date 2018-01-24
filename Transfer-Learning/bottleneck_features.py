from keras.applications.vgg16 import preprocess_input, VGG16
from keras.preprocessing import image
import numpy as np 
import glob 

img_paths = glob.glob("images/*.jpg")

def path_to_tensor(img_paths):
	# Load RGB image as PIL.Image.Image type 
	img = image.load_img(img_path, target_size=(224, 224))
	# Convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
	x = image.img_to_array(img)
	# Convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
	return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
	list_of_tensors = [path_to_tensor(img_path) for img_path in img_paths]
	return np.vstack(list_of_tensors)

img_input = preprocess_input(paths_to_tensor(img_paths))

#model = VGG16()
#model.summary()
#model.predict(img_input).shape

model = VGG16(include_top=False)
#mode.summary()

# Extract the output of final max pooling layer
print(model.predict(img_input).shape)