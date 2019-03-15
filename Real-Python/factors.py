# Take user input.
num = input("Enter a positive integer: ")

# Convert input from string to integer value.
num = int(num)

# Check for each number, from 1 to the input 'num', that is a divisor of 'num'
for i in range(1, num + 1):
    if (num % i) == 0:
        print(i, "is a divisor of", num)
