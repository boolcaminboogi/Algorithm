import heapq
class Node:
    def __init__(self, level, assigned, cost, reduced_matrix, path):
        self.level = level
        self.assigned = assigned
        self.cost = cost
        self.reduced_matrix = reduced_matrix
        self.path = path

    def __lt__(self, other):
        return self.cost < other.cost

def assignment_branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    initial_node = Node(0, [], 0, reduce_matrix(cost_matrix), [])
    min_cost = float('inf')
    min_assignment = None

    # Priority queue (min heap) to store nodes
    priority_queue = [initial_node]

    while priority_queue:
        node = heapq.heappop(priority_queue)
        level = node.level
        assigned = node.assigned
        current_cost = node.cost
        reduced_matrix = node.reduced_matrix
        path = node.path

        if level == n:
            if current_cost < min_cost:
                min_cost = current_cost
                min_assignment = assigned
            continue

        for i in range(n):
            if i not in assigned:
                new_assigned = assigned + [i]
                new_cost = current_cost + cost_matrix[level][i]
                new_reduced_matrix = reduce_matrix(reduced_matrix)
                new_reduced_cost = current_cost + new_reduced_matrix[level][i]
                new_path = path + [(level, i)]

                if new_reduced_cost < min_cost:
                    heapq.heappush(priority_queue, Node(level + 1, new_assigned, new_cost, new_reduced_matrix, new_path))

    return min_assignment, min_cost

def reduce_matrix(matrix):
    n = len(matrix)
    reduced_matrix = [row[:] for row in matrix]

    # Reduce rows
    for i in range(n):
        min_value = min(reduced_matrix[i])
        if min_value > 0:
            for j in range(n):
                reduced_matrix[i][j] -= min_value

    # Reduce columns
    for j in range(n):
        min_value = min(reduced_matrix[i][j] for i in range(n))
        if min_value > 0:
            for i in range(n):
                reduced_matrix[i][j] -= min_value
    return reduced_matrix

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

assignment, total_cost = assignment_branch_and_bound(cost_matrix)

print("Minimum Cost:", total_cost)
print("Assignment:", assignment)
