import random

lst = []
for i in range(20):
    lst.append(random.randint(0, 99))

print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)


