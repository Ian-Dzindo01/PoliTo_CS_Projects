cnt = 0
pin = '1234'

while(True):

    if cnt == 3:
        print("\nYour bank card is blocked!")
        break

    cnt += 1

    s1 = input("\nEnter PIN:")

    if str(s1) == pin:
        print("\nYour PIN is correct!")
        break

    else:
        print("\nYour PIN is incorrect!")
