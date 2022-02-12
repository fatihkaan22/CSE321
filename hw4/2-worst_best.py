def find_worst_and_best_dnc(arr, l, r, worst, best):
    if l == r:
        return min(worst, arr[l]), max(best, arr[l])

    if r - l == 1:
        return min(worst, arr[l], arr[r]), max(best, arr[l], arr[r])

    mid = (l + r) // 2
    worst, best = find_worst_and_best_dnc(arr, l, mid, worst, best)
    return find_worst_and_best_dnc(arr, mid + 1, r, worst, best)


def find_worst_and_best(arr):
    return find_worst_and_best_dnc(arr, 0, len(arr)-1, float('inf'), float('-inf'))


experiments = [-1, 1, 12, 18, 2, 3, 4, -9]

print(find_worst_and_best(experiments))
