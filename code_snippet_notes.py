from keras.models import Sequential
from keras.layers import Dense
"""
Suposse we had the sequence [1, 3, 5, 7, 9, 11, 13, 15] and want to find a 
function that generates it. 
"""

model = Sequential()

# g(s) = W0 + W1S the network output should be approx f(s) = 2+1S

# Fully connected layer
layer = Dense(1, input_dim=1, activation='linear')
model.add(layer)

# Compile and train the network
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x, y, epochs=3000, batch_size=3, callbacks=[], verbose=0)

# Print learned weights 
print(model.get_weights())


"""
Financial times series
"""
model = Sequential()
model.add(SimpleRNN(1, input_shape=(5,1)))
model.add(Dense(1))
model.compile(loss='meand_squared_error', optimizer='adam')