import random
def Main():
    was_es_Sein_soll = "laki"
    text = "Hallo Laki wie gehts was machst du kleiner Zwerg"
    list = []
    text.lower()
    list.append(text.split())
    for i in list:
        if i == was_es_Sein_soll:
            print(list[i])

Main()