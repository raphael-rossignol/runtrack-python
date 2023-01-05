def list():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    if "Mangue" not in fruits:
        fruits.insert(2, "Mangue")
    print(fruits)

list()