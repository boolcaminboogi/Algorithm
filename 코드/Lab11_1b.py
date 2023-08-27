def coin_change_dynamic(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        print("Cannot make exact change with the given coins.")
        return []

    change = []
    i = amount
    while i > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                change.append(coin)
                i -= coin
                break

    return change


# Testing the code
coins = [1, 5, 10, 25]
amount = 63

print("Coins:", coins)
print("Amount:", amount)
print("Change:", coin_change_dynamic(coins, amount))
