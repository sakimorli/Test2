import math
def Main():
    def POW(hoch_zahl, zahl):
        sum = 1
        for i in range(0, hoch_zahl):
            sum *= zahl
        print(sum)
    input1= input("Gib eine zahl ein: ")
    input2 = input("Gib eine hochzahl ein: ")
    POW(int(input2), int(input1))
    def SIN(grad):
        print(grad * (math.pi / 180))
    SIN(20)
    def WURZEL(zahl, hoch_zahl):
        sum = zahl
        for i in range(0, hoch_zahl):
            sum = zahl / hoch_zahl
        print(sum)
    WURZEL(4, 3)
Main()