theater = [[10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10],
           [10,10,20,20,20,20,20,20,10,10],
           [10,10,20,20,20,20,20,20,10,10],
           [10,10,20,20,20,20,20,20,10,10],
           [20,20,30,30,40,40,30,30,20,20],
           [20,30,30,40,50,50,40,30,30,20],
           [30,40,50,50,50,50,50,50,40,30]]

def printTheater():
    for row in theater:
        print(row)


def pFunction():
    while(True):
        printTheater()
        p = input("\nPlease enter a price: ")
        p = int(p)

        if p not in [10,20,30,40,50]:
            print("\nNo seats with that price. Please try again.\n")
            continue

        for i in range(len(theater)):
            for j in range(10):
                if theater[i][j] == p:
                    theater[i][j] = 0
                    return 0



def sFunction():
    while(True):
        printTheater()
        r = int(input("\nPlease enter seat row:"))
        s = int(input("\nPlease enter seat number:"))

        if s >= 9 or r >= 10 or s < 0 or r < 0:
            print("\nPlease enter a valid seat number.")


        if theater[r][s] == 0:
            print("\nThat seat is taken, please choose another one.")
            continue

        theater[r][s] = 0
        return 0


printTheater()

print("\nWould you like to pick by seat number or by price? \n")
c = input("\nPress P if you want to pick by price, or S if you want to pick by seat number:\n")

if c == 'S':
    sFunction()

if c == 'P':
    pFunction()

print("\nCongratulations, you have successfuly bought a ticket!\n")
printTheater()
