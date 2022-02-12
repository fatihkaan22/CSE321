def max_profit(profits):
    local_max = 0
    max_profit = profits[0]

    for i in range(0, len(profits)):
        local_max = max(profits[i], profits[i] + local_max)
        if local_max > max_profit:
            max_profit = local_max

    return max_profit


profits = [3, -5, 2, 11, -8, 9, -5]
print(max_profit(profits))
