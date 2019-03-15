# Ask for user input until condition is met then break from loop.
while True:
    userQuit = input("type 'q' to quit program: ")
    if userQuit.lower() == 'q':
        break

# Print all numbers except multiples of 3 using continue
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
