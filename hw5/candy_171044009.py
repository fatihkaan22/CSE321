def max_price(prices, n):
    memo = [0] * (n+1)

    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            current = prices[j] + memo[i-j-1]
            if (current > max_val):
                max_val = current
                memo[i] = max_val

    return memo[n]


prices = [1, 5, 8, 9, 10, 17, 17, 20]
print(max_price(prices, 8))
