x = input("Enter a number:")

def print_factors(x):
   print("The factors of ", x, " are:")
   for i in range(1, int(x) + 1):
       if int(x) % i == 0:
           print(i)

print_factors(x)
