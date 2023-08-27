import itertools


def assignment_brute_force(cost_matrix):
    n = len(cost_matrix)
    min_cost = float('inf')
    min_assignment = None

    # Generate all possible permutations of assignments
    assignments = list(itertools.permutations(range(n)))

    # Iterate through each permutation and calculate the total cost
    for assignment in assignments:
        total_cost = 0
        for i in range(n):
            total_cost += cost_matrix[i][assignment[i]]

        # Update minimum cost and assignment if a better solution is found
        if total_cost < min_cost:
            min_cost = total_cost
            min_assignment = assignment

    return min_assignment, min_cost


# Testing the code
cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

print("Cost Matrix:")
for row in cost_matrix:
    print(row)

assignment, total_cost = assignment_brute_force(cost_matrix)

print("Minimum Cost:", total_cost)
print("Assignment:", assignment)
