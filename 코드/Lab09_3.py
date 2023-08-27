def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m, n - 1), lcs_recursive(X, Y, m - 1, n))
        

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"

lcs_length = lcs_recursive(X, Y, len(X), len(Y))
print(f"Length of Longest Common Subsequence(Rec): {lcs_length}")


def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)

    # Create an (m+1) x (n+1) matrix for dynamic programming
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Compute the length of the LCS
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Example usage
X = "AGGTAB"
Y = "GXTXAYB"

lcs_length = lcs_dp(X, Y)
print(f"Length of Longest Common Subsequence(Dynamic): {lcs_length}")
