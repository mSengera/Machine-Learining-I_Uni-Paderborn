"""
Decide, which digit is written in bitmap (To check missmatch rate)
"""
def digit(line):
    if line < 51:
        return 0
    elif line < 101:
        return 1
    else:
        return 8

"""
Get hamming distance between two binary strings
"""
def hamming_dist(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

"""
Main Programm
"""
miss_counter = 0
digits = {}

with open("digits.txt", "rb") as f:
    for line_number, line in enumerate(f, 1):
        entry = line[:-1]
        digits[entry] = digit(line_number)

for digit in digits:
    min_distance = len(digit)
    target_category = -1

    for other in digits:
        if digit != other:
            distance = hamming_dist(digit, other)

            if distance < min_distance:
                min_distance = distance
                target_category = digits[other]

    if target_category != digits[digit]:
        miss_counter += 1
        print("Error: predicted class {0}, but in reality it's {1}".format(target_category, digits[digit]))

print("\n{0}% error rate. {1} missmatches in total. Dataset has {2} entries in total.".format(miss_counter / len(digits) * 100, miss_counter, len(digits)))