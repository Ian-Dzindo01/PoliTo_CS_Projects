# WORKS FOR ALL COMBINATIONS OF 4X4 MAGIC SQUARES!

def isMagic(m):
    lst = []
    for i in range(0, 16, 4):
        val = 0
        for j in range(0,4):
            val += m[i+j]

        lst.append(val)

    for i in range(0, 4):
        val = 0
        for j in range(i, i + 13, 4):
            val += m[j]

        lst.append(val)

    lst.append(m[0]+m[5]+m[10]+m[15])
    lst.append(m[3]+m[6]+m[9]+m[12])

    if len(set(lst)) == 1:
        return True

    return False

lst = []

print("Enter 16 numbers: ")

for i in range(16):
    lst.append(int(input()))

#smp = [*range(1,17,1)]

#if set(smp) != set(lst):
#    print('A magic square cannot be formed using these numbers!')

if isMagic(lst):
    print("Congratulations, you have a magic square!")
else:
    print("That is not a magic square!")
