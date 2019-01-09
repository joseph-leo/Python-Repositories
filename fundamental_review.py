print("\n# -- part 1 --#")

zero = 0
one = 23
two = [5, 4, 3, 2, 1]
three = "I love Python!"
three = three.split(" ")
four = [['P', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['h', 'u', 'r', 'd']]
five = {"happy":"birthday", "what's":"up", "fish":"chips"}
six = {1, 3, 4, 5, 6, 7, 8, 9, 10}
days = ("Fri", "Sat", "Wed")
x, y, seven = days

print("zero: {}".format(zero == 0))
print("one: {}".format(one > 22))
print("two: {}".format(len(two) == 5))
print("three: {}".format(three[2] == "Python!"))
print("five:  {}".format(five.get("fish") == "chips"))
print("five: {}".format(len(five) == 3))
print("six: {}".format(len(six & {2,5,7}) == 2))
print("seven: {}".format(seven == "Wed"))


print("\n# -- part 2 --#")

value = [5, 9, 1, -1]

if type(value) is list:
    print(True)
else:
    print(False)

for x in value:
    if not type(x) is int:
        print(False)
    else:
        print(True)

num = 0
while num < value[2]:
    print(True)
    num += 1

for y in range(value[3]):
    if y in value:
        print(False)

try:
    value[5] = "Cat"
    while True:
        print(False)
except IndexError:
    print(True)

try:
    assert value[3] == -1
except AssertionError:
    print(True)
