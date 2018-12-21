# Prints even numbers through 10 using a for loop.
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print("done with for loop.")

# Prints even numbers through 10 using a while loop.
n = 1
while (n <= 10):
    if n % 2 == 0:
        print(n)
    n += 1
print("done with while loop.")

# Doubles a number 3 times using a for loop
def doubles(num):
    for i in range(1, 4):
        num *= 2
        print(num)
    return

doubles(2)
        
