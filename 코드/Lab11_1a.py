def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # Sort the coins in descending order
    change = []
    total = 0
    
    for coin in coins:
        while total + coin <= amount:
            change.append(coin)
            total += coin
    
    if total != amount:
        print("Cannot make exact change with the given coins.")
    
    return change


# Testing the code
coins = [1, 5, 10, 25]
amount = 63

print("Coins:", coins)
print("Amount:", amount)
print("Change:", coin_change_greedy(coins, amount))
