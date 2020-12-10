def nameOfBestCustomer(s, p):
    ind = p.index(max(p))
    print("And the best customer is... \n")
    print(s[ind], ' = ', p[ind], '\n')

def printD(s, p):
    for i in range(len(s)):
        print(s[i], '=', p[i], '\n')


print('Hi there. Please enter all the customers names and their purchase amounts.')

print("When you do not have anymore customers, just type in 'break' in the name field to terminate the program.")

names = []
prices = []

while(True):
    name = input("Name: \n")
    if name == 'break':
        break

    price = int(input("Price: \n"))

    names.append(name)
    prices.append(price)


printD(names, prices)

nameOfBestCustomer(names, prices)






