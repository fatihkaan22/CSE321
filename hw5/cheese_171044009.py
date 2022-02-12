def find_max_price(prices, weights, capacity):
    indices = list(range(len(prices)))
    costs = [v/w for v, w in zip(prices, weights)]

    def get_cost(i):
        return costs[i]

    # TODO: do we need to sort all array?
    # consider getting max at each step
    indices.sort(key=get_cost, reverse=True)

    max_value = 0
    for i in indices:
        if weights[i] <= capacity:
            max_value += prices[i]
            capacity -= weights[i]
        else:
            max_value += prices[i]*capacity/weights[i]
            break

    return max_value


weights = [1, 4, 2, 3]
values = [6, 4, 8, 10]
capacity = 60

print(find_max_price(values, weights, capacity))
