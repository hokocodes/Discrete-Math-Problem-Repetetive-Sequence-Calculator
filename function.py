def f(start):

    i = 0

    while i < 100:
        if start % 2 == 0:
            y = start/2
            print(f'{start}' + " / 2 = " + str(y))
            start = y
        elif start % 2 != 0:
            z = start * 3 + 1
            print(f'{start}' + " * 3 + 1 " + str(z))
            start = z
        i += 1


f(15)
