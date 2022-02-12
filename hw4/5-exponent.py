def exponentiation_bf(a, n):
    r = 1
    for _ in range(n):
        r *= a
    return r


def exponentiation_dnc(a, n):
    if n == 1:
        return a
    k = n//2
    return exponentiation_dnc(a, k) * exponentiation_dnc(a, n-k)


print(exponentiation_bf(2, 5))
print(exponentiation_dnc(2, 5))
