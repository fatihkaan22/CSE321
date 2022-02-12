def min_cuts(length):
    if (length == 1):
        return 0
    part1 = length // 2
    part2 = length - part1  # longer or equal part
    return 1 + min_cuts(part2)


print(min_cuts(100))
