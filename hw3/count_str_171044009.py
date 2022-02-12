def numberOfSubstrings(string, startsWith, endsWith):
    count = 0;
    for i in range(0, len(string)):
        if (string[i] == startsWith):
            for j in range(i, len(string)):
                if (string[j] == endsWith):
                    count = count + 1;
    return count


print(numberOfSubstrings('TXZXXJZWX' , 'X', 'Z'))

# worst case
# print(numberOfSubstrings('XXXXXX' , 'X', 'X'))
