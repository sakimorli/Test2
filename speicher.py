def Main():
    #das könnte deinen code verbessern
    string = ""
    int = 0
    for i in range(0,10):
        string += "a"
        if string == "aaaa":
            for i in range(0, 6):
                int += 1
                print(int)
                if int == 4:
                    print("du hast es geschafft")
        print(string)
    #so kannst du schleifen benutzten
Main()