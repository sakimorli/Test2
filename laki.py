def Main():
    for i in range(2, 26):
        ist_true = True
        for j in range(2, int(i ** 0.5)+ 1):
            if i % j == 0:
                ist_true = False
                break
        if ist_true:
            print(i)
<<<<<<< HEAD
Main()
=======
Main()
>>>>>>> 2567b634ee44b0943ca5cb71fb36620fa463db37
