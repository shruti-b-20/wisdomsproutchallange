def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# --- Test Cases ---
print(fibonacci(5))     # Output: 5
print(fibonacci(10))    # Output: 55
print(fibonacci(0))     # Output: 0
print(fibonacci(1000))  # Output: Very large integer
