def FahrToCelsius(Fahrenheit):
    C = (F - 32) * (5/9)
    return C

def CelsiusToFahr(Celsius):
    F = C * (9/5) + 32
    return F

F = input("Convert Fahrenheit to Celsius: ")
F = float(F)
print(FahrToCelsius(F))

C = input("Convert Celsius to Fahrenheit: ")
C = float(C)
print(CelsiusToFahr(C))
