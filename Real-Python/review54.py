n1 = 8
n2 = 5
n3 = 2

def cube(num):
    """Takes a number and multiples
    it by itself"""
    total = num * num
    return total

print(f"""{n1}, {n2}, and {n3} squared =
{cube(n1)}, {cube(n2)}, and {cube(n3)} respectively.""")


def multiply(num1, num2):
    """Multiplies two numbers"""
    total = num1 * num2
    return total

outputNum = multiply(2, 5)
print(""" 
""" + str(outputNum))
