def draw_rectangle():
    width = int(input("largeur : "))
    height = int(input("hauteur : "))

    char1 = '-' * width
    char2 = '|'
    sharp = '#' * width
    blank = ' '

    line = char2 + char1 + char2
    line2 = char2 + sharp + char2

    print(line)
    x = 0
    while x != height:
        print(line2)
        x += 1
    print(line)

draw_rectangle()