def rop(arr):
    if len(arr) <= 1:
        return 0
    rop_count = 0
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    rop_count += rop(L)
    rop_count += rop(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            rop_count += (len(L) - i)
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return rop_count


arr = [9, 7, 3, 2]
print(rop(arr))
