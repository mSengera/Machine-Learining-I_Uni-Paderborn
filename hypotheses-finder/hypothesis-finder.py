import matplotlib.pyplot as plt

"""
Function to draw a rectangle in matplotlib
"""
def draw_rectangle(y_min, y_max, x_min, x_max):
    plt.hlines(y_min, x_min, x_max)
    plt.hlines(y_max, x_min, x_max)
    plt.vlines(x_min, y_min, y_max)
    plt.vlines(x_max, y_min, y_max)

"""
Training Data for the learner
"""
training_data = [
    [[4, 6], 1],
    [[4, 1], 1],
    [[2, 3], 1],
    [[1, 2], 1],
    [[2, 4], 1],
    [[2, 1], 1],
    [[5, 7], -1],
    [[6, 3], -1],
    [[4, 2], -1],
    [[3, 3], -1],
    [[2, 5], -1],
    [[5, 5], -1]
]

"""
Plot training data
"""
for point in training_data:
    if point[1] == 1:
        plt.plot(point[0][0], point[0][1], "+g")
    else:
        plt.plot(point[0][0], point[0][1], ".r")

"""
Initial hypotheses (ALL + points)
"""
y_min = 999
y_max = 0
x_min = 999
x_max = 0

for point in training_data:
    if point[1] == 1:
        if point[0][0] < x_min:
            x_min = point[0][0]

        if point[0][0] > x_max:
            x_max = point[0][0]

        if point[0][1] < y_min:
            y_min = point[0][1]

        if point[0][1] > y_max:
            y_max = point[0][1]

draw_rectangle(y_min, y_max, x_min, x_max)

"""
Check Hypotheses
"""
missmatches = 0
matches = 0

for point in training_data:
    contains = False

    if x_min <= point[0][0] <= x_max and y_min <= point[0][1] <= y_max:
        contains = True

    if contains:
        if point[1] == -1:
            missmatches = missmatches + 1
        else:
            matches = matches + 1

print("Missmatches: "+ str(missmatches))
print("Matches: "+ str(matches))

# Plot the coordinate system
plt.show()