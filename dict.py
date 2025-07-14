def Main():
    dict= {}
    list = ["Daniel", "Lazar", "Sava", "Jefimija"]
    for list1 in list:
        frage = input(f"Welches Kind ist {list1}: ")
        dict[list1] = frage
    inf = 0
    parsed_frage = int(dict[list1])
    for i in range (0, len(frage) + 1):
        if inf < parsed_frage:
            inf = dict[list1]
        print(f"{dict[list1]} ist das älteste Kind in der Familie")
    print(dict)
Main()