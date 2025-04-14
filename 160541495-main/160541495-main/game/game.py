import random
while True:
    try:
        x=int(input("Level: "))
        if int(x)>0:
            break
        else:
            continue

    except ValueError:
        continue
    
r=random.randint(1,x)

while True:
    try:
        y=int(input("Guess: "))
        if int(y)>0:
            if y<r:
                print("Too small!")
            elif y>r:
                print("Too large!")
            elif y==r:
                print("Just right!")
                break
        else:
            continue
    except ValueError:
        continue



