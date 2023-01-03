def Légume():
    type = "fruits"
    saison = "hiver"
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinamboure, endive")
    elif type == "legumes" and saison == "été":
        print("artichaut, aubergine, navet")

Légume()