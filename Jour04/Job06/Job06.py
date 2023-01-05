L = [1, 2, 3, 4, 5]
def list():
    L
    first = L[0]
    last = L[4]
    L[0] = last
    L[4] = first
    print(L)

list()