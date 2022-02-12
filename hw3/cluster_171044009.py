regions = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
profits = [3, -5, 2, 11, -8, 9, -5]

# brute force algorithm


def mostProfitableClusterBF(regions, profits):
    maxProfit = profits[0]
    cluster = [regions[0]]

    for i in range(0, len(regions)):
        for j in range(i, len(regions)):
            p = sum(profits[i:j])
            if maxProfit < p:
                maxProfit = p
                cluster = regions[i:j]

    return cluster


print(mostProfitableClusterBF(regions, profits))

# divide & conquer algorithm


def maxProfitCrossing(profits, start, middle, end):
    s = 0
    leftSum = rightSum = float('-inf')

    for i in range(middle, start-1, -1):
        s = s + profits[i]
        if (s > leftSum):
            leftSum = s

    s = 0
    for i in range(middle + 1, end + 1):
        s = s + profits[i]
        if (s > rightSum):
            rightSum = s

    return max(leftSum + rightSum, leftSum, rightSum)


def maxProfitDNC(profits, start, end):
    if (start == end):
        return profits[start]

    middle = (start + end) // 2

    return max(maxProfitDNC(profits, start, middle),
               maxProfitDNC(profits, middle+1, end),
               maxProfitCrossing(profits, start, middle, end))


def maxProfit(profits):
    return maxProfitDNC(profits, 0, len(profits) - 1)


print(maxProfit(profits))
