remaining = 100
buyers = 0

while(remaining > 0):
    print("\nNumber of available tickets: " + str(remaining))
    x = input("\nEnter the number of tickets you want to buy:")
    if int(x) > 4:
        print("\nYou cannot buy more than 4 tickets at a time!")
        continue
    elif (remaining - int(x)) < 0:
        print("\nWe do not have that many tickets left!")
        continue

    remaining -= int(x)
    print("\nYou have successfully purchased " + str(x) + " tickets!")
    buyers += 1

print("\nThere were " + str(buyers) + " buyers!")
