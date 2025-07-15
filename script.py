def Main():
    was_es_Sein_soll = "laki"
    text = "Hallo Laki wie gehts was machst du kleiner Zwerg"
    text1 = text.lower()
    word = text1.split()
    for i in word:
        if was_es_Sein_soll == i:
            print(i)
Main()
