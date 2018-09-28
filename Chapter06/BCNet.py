import numpy
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
numpy.random.seed(1)
dataset = numpy.loadtxt("BreastCancer.csv", delimiter=",")
X = dataset[:,1:10]
Y = dataset[:,10]
X = (X - numpy.min(X, 0)) / (numpy.max(X, 0) - numpy.min(X, 0))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
model = Sequential()
model.add(Dense(10, input_dim=9, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=200, batch_size=10)
ResultEval = model.evaluate(X_test, Y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], ResultEval [1]*100))
