def premier():
    for i in range(2, 1000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

premier()