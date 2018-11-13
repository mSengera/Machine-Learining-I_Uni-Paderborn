"""
The Abalone Dataset
"""
from scipy.spatial import distance
import operator
import sys

k = 30  # Number of neighbours to calc. See table for error rate.
"""
--------------------------
-- k --- Error rate ------
--------------------------
-- 5 --- 2.9480 ----------
-- 10 -- 2.3832 ----------
-- 15 -- 2.4838 ----------
-- 20 -- 2.3918 ----------
-- 25 -- 2.2965 ---------- 
-- 30 -- 2.2843 ----------
-- 35 -- 2.2916 ----------
-- 40 -- 2.3187 ----------
-- 45 -- 2.3533 ----------
-- 50 -- 2.3032 ----------
--------------------------
"""

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
    i = i + 1
    sys.stdout.write('\rProgress: ' + str(round(i / num_lines * 100)) + '%')

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

    top = sorted(nn, key=operator.itemgetter(0))[:k]  # Grab k best abalone data

    # Get total rings count
    rings = 0.0
    for abalone in top:
        rings = rings + float(abalone[1][-1])

    error_distance = abs((rings / k) - (float(x[-1])))
    error_count = error_count + error_distance

print('\nAverage mistake: ' + str(error_count / num_lines))
