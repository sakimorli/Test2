def Main():
    def shakra(lvl):
        lvl1 = int(lvl)
        for i in range(0, lvl1, 10):
            if lvl1 >= 100:
                print("rasengan")
            elif lvl1 < 100 and lvl1 >= 25:
                print("schatten doppelgänger")
            elif lvl1 <= 0:
                print("pause")
                lvl1 += 100
            else:
                print("fehler")
            lvl1 -= 15
    input1 = input("Wie groß ist dein Shakra: ")
    shakra(input1)

Main()