from itertools import chain, combinations

"""
Copy the input from exercise cheet
"""
# [x0, x1, x2], [probability_positive, probability_negative]
probability_distribution = [
    [[0, 0, 0], [0.08, 0.02]],
    [[1, 0, 0], [0.14, 0.06]],
    [[0, 1, 0], [0.09, 0.01]],
    [[0, 0, 1], [0.12, 0.08]],
    [[1, 1, 0], [0.04, 0.06]],
    [[1, 0, 1], [0.01, 0.09]],
    [[0, 1, 1], [0.05, 0.05]],
    [[1, 1, 1], [0.02, 0.08]]
]


def powerset(iterable):
    # powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)

    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


class Hypothesis:

    def __init__(self, a, t):
        self.a = a
        self.t = t
        self.risk = round(self.calculate_true_risk(), 2)

    def __str__(self):
        return "A = {}, t = {}, (true) risk = {}".format(self.a, self.t, self.risk)

    def predict(self, x):
        summation = sum([x[i] for i in range(len(self.a))])

        return 1 if summation >= self.t else -1

    def calculate_true_risk(self):
        risk = 0

        for x, (prob_negative, prob_positive) in probability_distribution:
            if self.predict(x) == 1:
                risk += 1 * prob_negative + 0 * prob_positive
            else:
                risk += 1 * prob_positive + 0 * prob_negative

        return risk


def generate_hypothesis_space():
    hypos = []

    for a in powerset({1, 2, 3}):
        for t in [i for i in range(len(a) + 2)]:
            hypos.append(Hypothesis(a, t))

    return hypos


H = generate_hypothesis_space()
H.sort(key=lambda k: k.risk)

for h in H[:]:
    print(h)
    for x, y in probability_distribution:
        print("\t {} -> {}".format(x, h.predict(x)))
