def rng(rold):
    a = 32310901
    b = 1729
    m = 2**24

    for i in range(100):
        rnew = (a*int(rold) + b)%m
        rold = rnew
        print(rnew)

x = input("Enter a seed number:")
rng(x)
