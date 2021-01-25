l = []
cnt = 2

print("Please input 10 floating point values: ")

while(True):
    try:
        x = float(input())
    except ValueError:
        print("Please input a floating point number.\n")
        cnt -= 1

        if cnt == 0:
            print("No more input tries left. Proceeding with the given values.\n")
            break

        print("You have ", cnt, " try left.")
        continue

    l.append(float(x))


print("The sum of the given values is: ", sum(l))
