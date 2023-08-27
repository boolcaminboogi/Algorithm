def coin_change_branch_and_bound(coins, amount):
    coins.sort(reverse=True)  # Sort the coins in descending order
    n = len(coins)
    min_coins = float('inf')
    result = []
    current_combination = []

    def backtrack(start_index, remaining_amount, num_coins):
        nonlocal min_coins, result, current_combination

        if remaining_amount == 0 and num_coins < min_coins:
            min_coins = num_coins
            result = current_combination[:]
            return

        if start_index == n or remaining_amount < 0 or num_coins >= min_coins:
            return

        max_coin = remaining_amount // coins[start_index]
        for i in range(max_coin, -1, -1):
            current_combination.append(coins[start_index] * i)
            backtrack(start_index + 1, remaining_amount - coins[start_index] * i, num_coins + i)
            current_combination.pop()

    backtrack(0, amount, 0)
    return result


# Testing the code
coins = [1, 5, 10, 25]
amount = 63

print("Coins:", coins)
print("Amount:", amount)
print("Optimal Combination:", coin_change_branch_and_bound(coins, amount))
