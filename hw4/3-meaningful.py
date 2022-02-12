def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def first_meaningful_h(arr, k, l, h):
    print('y')
    if (k > 0 and k <= h - l + 1):
        pivot_i = partition(arr, l, h)

        distance = pivot_i - l + 1 - k

        if (distance == 0):
            return arr[pivot_i]

        if (distance < 0):
            return first_meaningful_h(arr, -distance, pivot_i + 1, h)
        return first_meaningful_h(arr, k, l, pivot_i - 1)


def first_meaningful(arr, k):
    return first_meaningful_h(arr, k, 0, len(arr) - 1)


arr = [9, 3, 7, 6, 2, 12, 13, 4]
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(first_meaningful(arr, 8))

# merge sort

