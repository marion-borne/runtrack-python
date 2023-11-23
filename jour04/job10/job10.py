def multiple():
    L = [8,24,27,48,2,16,9,102,7,84,91]
    result = 1
    for num in L:
        if 24 < num < 91:
            result *= num
    return result

print (multiple())
