desserts = ['ice cream', 'cookies']

desserts.sort()
print(desserts)

print(desserts.index('ice cream'))

food = []
food.extend(desserts)
food.extend(['broccoli', 'turnips'])

print(desserts)
print(food)

food.remove('cookies')
print(food)

print(food[:2])

cookies = "cookies, cookies, cookies"
breakfast = []
breakfast = cookies.split(", ")
print(breakfast)

def oneThruTwenty(numList):
    newList = []
    for i in numList:
        if i <= 20:
            newList.append(i)
    print(newList)

nums = [2, 4, 8, 16, 32, 64]
oneThruTwenty(nums)
            

