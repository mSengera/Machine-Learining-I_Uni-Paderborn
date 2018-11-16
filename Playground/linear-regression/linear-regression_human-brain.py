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



