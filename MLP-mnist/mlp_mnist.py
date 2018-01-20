from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential 
from keras.layers import Dense, Dropout, Flatten
from keras.callbacks import ModelCheckpoint 
'''
Multi-layer perceptron to decode images of handwritten numerical digits. 
'''

# Use keras to import pre-shuffled MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Rescale [0, 255] --> [0, 1]
X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255

# One-hot encode the labels
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# Define the model
model = Sequential()
model.add(Flatten(input_shape=X_train.shape[1:]))
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(10, activation="softmax"))

# Summarize the model 
model.summary()

# Compile the model 
model.compile(loss="categorical_crossentropy", optimizer="rmsprop", metrics=["accuracy"])

# Calculate the classification accuracy on the test set (Before training)
score = model.evaluate(X_test, y_test, verbose=0)
accuracy = 100*score[1]
print("Test accuracy before training: %.4f%%" % accuracy)


# Train the model 
# Save the model weights to get the best accuracy on the validation set after each epoch
checkpointer = ModelCheckpoint(filepath='mnist.model.best.hdf5', verbose=1, save_best_only=True)
hist = model.fit(X_train, y_train, batch_size=128, epochs=10, validation_split=0.2, 
				 callbacks=[checkpointer], verbose=1, shuffle=True)

# Load the weights that yielded the best validation accuracy
model.load_weights('mnist.model.best.hdf5')

# Evaluate the accuracy
score = model.evaluate(X_test, y_test, verbose=0)
accuracy = 100*score[1]
print("Test accuracy after training: %.4f%%" % accuracy)