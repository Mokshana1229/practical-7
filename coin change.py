def make_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]

coins = [2, 6, 10, 25]
amount = 36

print("Minimum number of coins:", make_change(coins, amount))
