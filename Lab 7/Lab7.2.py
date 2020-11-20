import random

s1 = 0
lst = []
for x in range(random.randint(1, 22)):
    lst.append(random.randint(0, 100))

print(lst)

for x in range(len(lst)):
    if x%2 == 0:
        s1 += lst[x]
    else:
        s1 -= lst[x]

print("The alternating sum is: ", s1)



