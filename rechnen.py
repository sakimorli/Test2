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
    def SIN(grad, gk, ak):
        sin = 0
        sum = 0
        sum = (gk / ak)
        sin = grad * (math.pi / 180)
        print(sum)
    SIN(20,3,4)
Main()