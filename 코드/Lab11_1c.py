def coin_change_backtracking(coins, amount):
    coins.sort(reverse=True)  # Sort the coins in descending order
    result = []
    backtrack(coins, amount, [], result)
    return result


def backtrack(coins, amount, current_combination, result):
    if amount == 0:
        result.append(current_combination)
        return

    if amount < 0:
        return

    for i in range(len(coins)):
        coin = coins[i]
        if coin > amount:
            continue
        backtrack(coins[i:], amount - coin, current_combination + [coin], result)


# Testing the code
coins = [1, 5, 10, 25]
amount = 63

print("Coins:", coins)
print("Amount:", amount)
print("Possible Combinations:")
combinations = coin_change_backtracking(coins, amount)
for combination in combinations:
    print(combination)
