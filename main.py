def min_coins(coins, target_amount):
    # Initialize dp array where dp[i] will be the minimum coins to make amount i
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  # Base case: No coins are needed to make amount 0
    
    # Loop over all coins
    for coin in coins:
        for i in range(coin, target_amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[target_amount] is still infinity, return -1 as it's not possible
    return dp[target_amount] if dp[target_amount] != float('inf') else -1

# Example usage
coins = [1, 4, 6, 9, 14]
target_amount = 26
print(min_coins(coins, target_amount))  # Output: 3
