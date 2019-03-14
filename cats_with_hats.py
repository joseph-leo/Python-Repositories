


cats = []
for i in range(0, 100):
    cats.append(0)

for rounds in range(0, len(cats)):
    roundCheck = rounds + 1
    for stop in range(0, len(cats)):
        cat = cats[stop]
        stopCheck = stop + 1
        if (stopCheck % roundCheck == 0):
            if (cat == 0):
                cats[stop] += 1
            else:
                cats[stop] -= 1

count = 1
for hat in cats:
    if (hat == 1):
        print("Cat: " + str(count) + " has a hat")
    count += 1

print("All perfect squares!")
        

            
                    
    
