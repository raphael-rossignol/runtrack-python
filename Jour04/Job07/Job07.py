def list():
    L = [8, 24, 48, 2, 16, 7]
    i = 0
    j = 0
    while i < len(L):
        if L[i] % 3 == 0:
            j = j + 1
        i = i + 1
    print(j)

list()