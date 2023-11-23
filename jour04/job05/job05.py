def Liste():
    L = [1,2,3,4,5]
    print(L)
    print(L[2])
    L[3] = L[2] + L[4]
    print(L)
    return L[4]

print (Liste())
