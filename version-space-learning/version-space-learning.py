import matplotlib.pyplot as plt
import copy

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
    [[2, 3], 1],
    [[2, 1], 1],
    [[3, 4], 1],
    [[3, 5], 1],
    [[3, 2], 1],
    [[5, 7], 1],
    [[5, 2], 1],
    [[1, 2], 1],
    [[1, 1], -1],
    [[2, 1], -1],
    [[2, 5], -1],
    [[6, 8], -1],
    [[7, 4], -1],
    [[5, 3], -1],
    [[4, 4], -1],
    [[3, 6], -1],
    [[6, 4], -1]
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
S - Most specific boundary
"""
s_max_x = 0
s_min_x = 999
s_max_y = 0
s_min_y = 999

for point in training_data:
    old_s_max_x = copy.copy(s_max_x)
    old_s_min_x = copy.copy(s_min_x)
    old_s_max_y = copy.copy(s_max_y)
    old_s_min_y = copy.copy(s_min_y)

    if point[1] == 1:
        # positive
        if point[0][0] > s_max_x:
            s_max_x = point[0][0]

        if point[0][0] < s_min_x:
            s_min_x = point[0][0]

        if point[0][1] > s_max_y:
            s_max_y = point[0][1]

        if point[0][1] < s_min_y:
            s_min_y = point[0][1]

    """
    Check new S for violations
    """
    reset = False

    for point2 in training_data:
        if s_min_x <= point2[0][0] <= s_max_x and s_min_y <= point2[0][1] <= s_max_y and point2[1] == -1:
            reset = True
            break

    if reset:
        s_max_x = old_s_max_x
        s_min_x = old_s_min_x
        s_max_y = old_s_max_y
        s_min_y = old_s_min_y

draw_rectangle(s_min_y, s_max_y, s_min_x, s_max_x)

"""
G - Most general boundary
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

plt.show()