def Main():
    for i in range(2, 26):
        ist_true = True
        for j in range(2, int(i ** 0.5)+ 1):
            if i % j == 0:
                ist_true = False
                break
        if ist_true:
            print(i)
Main()
