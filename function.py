def f(start):

    i = 0

    while i < 100:
        if start % 2 == 0: #if it is even
            y = start/2
            print(f'{start}' + " / 2 = " + str(y)) #generate (recursively) a sequence of positive integers
            start = y
        elif start % 2 != 0: #if it is odd
            z = start * 3 + 1
            print(f'{start}' + " * 3 + 1 " + str(z)) #generate (recursively) a sequence of positive integers
            start = z
        i += 1


f(15)
