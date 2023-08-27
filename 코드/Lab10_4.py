import sys

class SumSubSet:
    def __init__(self, set, W):
        total = sum(set)
        n = len(set)
        include = []
        self.sumSS(set, include, 0, 0, n, W, total)

    def sumSS(self, set, include, index, weight, n, W, total):
        if weight == W:
            print("Subset =", include, "and the sum of the subset is =", sum(include))
            return
        elif index == n:
            return
        elif weight > W and total < W:
            return
        else:
            total -= set[index]
            self.sumSS(set, include, index + 1, weight, n, W, total)
            total += set[index]
            weight += set[index]
            include.append(set[index])
            self.sumSS(set, include, index + 1, weight, n, W, total)
            include.pop()

# Create an instance of SumSubSet
set = [1, 3, 5, 7, 9]
target_sum = 10
subset_sum = SumSubSet(set, target_sum)

