import random

lst = []
for x in range(11):
    lst.append(random.randint(0, 10000000))

print(lst)
lst.reverse()
print(lst)
print("First value: ", lst[0], " and last value: ", lst[len(lst) - 1])
