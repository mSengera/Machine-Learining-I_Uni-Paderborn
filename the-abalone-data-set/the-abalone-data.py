"""
Complete Dataset
"""
#fh = open('abalone.data')

"""
Small Dataset
"""
fh = open('abalone.small.data')

for line in fh:
    data = line.rstrip().split(',')
    print(data)

fh.close()