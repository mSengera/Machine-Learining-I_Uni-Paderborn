import copy

"""
The Abalone Dataset
"""
# Number of neighbours to calc
k = 20


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def dist(x_ori, y_ori):
    x = copy.deepcopy(x_ori)
    y = copy.deepcopy(y_ori)

    # Except rings attribute
    del x[-1]
    del y[-1]

    s = 0

    if len(x) == len(y):
        for index, value in enumerate(x):
            if isfloat(value) and isfloat(y[index]):
                s = s + (float(value) - float(y[index]))

    return s


"""
Complete Dataset
"""
path = 'abalone.data'

"""
Small Dataset
"""
#path = 'abalone.small.data'

error_count = 0
num_lines = sum(1 for l in open(path))
i = 0

for line in open(path):
    i = i + 1
    print(i)

    nn = []
    x = line.rstrip().split(',')

    for line2 in open(path):
        y = line2.rstrip().split(',')

        # Only check if data is differently
        if x == y:
            break

        # Only check if abalone is same gender
        if x[0] == y[0]:
            curr_dist = dist(x, y)
            nn.append([curr_dist, y])

    sorted_nn = sorted(nn)
    top = sorted_nn[:k]  # Grab the best k abalones

    rings = 0

    # Get average rings
    for abalone in top:
        rings = rings + int(abalone[1][-1])

    # Average rings
    rings = rings / k

    error_distance = (rings + 1.5) - (int(x[-1]) + 1.5)

    if error_distance < 0:
        error_distance = error_distance * -1

    error_count = error_count + error_distance

print('Average mistake: ' + str(error_count / num_lines))
