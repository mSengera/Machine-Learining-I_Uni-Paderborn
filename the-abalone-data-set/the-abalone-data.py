from scipy.spatial import distance

"""
The Abalone Dataset
"""
# Number of neighbours to calc
k = 20

# Complete Data Path
path = 'abalone.data'

# Small Data Path
# path = 'abalone.small.data'


def dist(x, y):
    return distance.euclidean([float(i) for j in x[1:-1]], [float(i) for k in y[1:-1]])


error_count = 0
num_lines = sum(1 for l in open(path))
i = 0

for line in open(path):
    # Print actual abalone data line
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

    rings = 0.0

    # Get average rings
    for abalone in top:
        rings = rings + float(abalone[1][-1])

    # Average rings
    rings = rings / k

    error_distance = abs((rings + 1.5) - (float(x[-1]) + 1.5))
    error_count = error_count + error_distance

print('Average mistake: ' + str(error_count / num_lines))
