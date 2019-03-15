# Boolean variable to check if loop should continue.
intCheck = False

# Continues loop if there is a non-integer input.
while (intCheck == False):
    try:
        num = int(input("Enter an integer: "))
        print(num)
        intCheck = True
    except ValueError:
        print("Try again.")
            
