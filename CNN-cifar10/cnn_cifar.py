from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from keras.datasets import cifar10
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint, EarlyStopping

# Load the pre-shuffled train and test data
(x_train, y_train),(x_test, y_test) = cifar10.load_data()

# Rescale the images 
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255

# One hot encode the labes
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# break training set into training and validation sets
# 45000 train samples, 10000 test samples, 5000 validation samples
(x_train, x_validation) = x_train[5000:], x_train[:5000]
(y_train, y_validation) = y_train[5000:], y_train[:5000]

# Define the model architecture
model = Sequential()

model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu', input_shape=(32,32,3)))
model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.25))

model.add(Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(10, activation='softmax'))

# model.summary()
# Compile the model 
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# Train the model
checkpointer = ModelCheckpoint(filepath='./cnncifar.weights.best.hdf5', verbose=1, save_best_only=True)
earlystop = EarlyStopping(patience=10)

hist = model.fit(x_train, y_train, batch_size=32, epochs=100, validation_data=(x_validation, y_validation),
				 callbacks=[checkpointer, earlystop], verbose=2, shuffle=True)

# Load the weights that yielded the best validation accuracy
model.load_weights('./cnncifar.weights.best.hdf5')

# Evaluate and print test accuracy
score = model.evaluate(x_test, y_test, verbose=0)
print('Test accuracy: ', score[1])

