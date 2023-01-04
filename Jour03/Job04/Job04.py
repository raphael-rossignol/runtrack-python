def loopfizz():
    i = 0
    while i < 100:
        i += 1
        if i % 15 == 0:
            print("BuzzFizz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        print(i)

loopfizz()