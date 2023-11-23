def multiple():
    L = [8,24,48,2,16]
    return sum(1 for num in L if num %3 == 0)

print (multiple())



