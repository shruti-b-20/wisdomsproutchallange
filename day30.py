def coinChange(coins, amount):
    # Initialize dp array with infinity
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0   # Base case: 0 coins needed for amount 0
    
    # Build dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != amount + 1 else -1

print(coinChange([1, 2, 5], 11))  # Output: 3  (5+5+1)
print(coinChange([2], 3))         # Output: -1
print(coinChange([1], 0))         # Output: 0
print(coinChange([1, 3, 4], 6))   # Output: 2  (3+3 or 4+1+1)
