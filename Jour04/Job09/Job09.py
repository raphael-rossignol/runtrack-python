def list():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    max = 0
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
            min = max
    for i in range(len(L)):
        if min > L[i]:
            min = L[i]
    print(min)
    print(max)

list()