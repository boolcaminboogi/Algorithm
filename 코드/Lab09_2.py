def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a distance matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute the minimum edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,         # Deletion
                dp[i][j - 1] + 1,         # Insertion
                dp[i - 1][j - 1] + cost   # Substitution
            )

    return dp[m][n]


# Example usage
s1 = "kitten"
s2 = "sitting"

distance = levenshtein_distance(s1, s2)
print(f"Levenshtein Distance between '{s1}' and '{s2}': {distance}")
