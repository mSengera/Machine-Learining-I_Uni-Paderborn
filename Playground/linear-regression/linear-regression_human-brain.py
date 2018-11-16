import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data/human-brain.csv')

# Printing the dataset dimensions
print(dataset.shape)

dataset.head()

# initializing our inputs and outputs
X = dataset['Head Size(cm^3)'].values
Y = dataset['Brain Weight(grams)'].values

# mean of our inputs and outputs
x_mean = np.mean(X)
y_mean = np.mean(Y)

# total number of values
n = len(X)

# using the formula to calculate the b1 and b0
numerator = 0
denominator = 0

for i in range(n):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2

b1 = numerator / denominator
b0 = y_mean - (b1 * x_mean)

# printing the coefficient
print(b1, b0)

# plotting values
x_max = np.max(X) + 100
x_min = np.min(X) - 100

# calculating line values of x and y
x = np.linspace(x_min, x_max, 1000)
y = b0 + b1 * x

# plotting line
plt.plot(x, y, color='#00ff00', label='Linear Regression')

# plot the data point
plt.scatter(X, Y, color='#ff0000', label='Data Point')

plt.xlabel('Head Size (cm^3)')
plt.ylabel('Brain Weight (grams)')

plt.legend()
plt.show()

