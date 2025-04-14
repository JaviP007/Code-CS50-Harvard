a=50
while True:
    x=int(input("Insert Coin: "))
    if x ==10 or x ==5 or x ==25:
        a=a-x
        if a>0:
            print(f"Amount Due: {a}")

    else:
        print(f"Amount Due: {a}")
        continue
    if a<=0:
        print(f"Change Owed: {a*-1}")
        break

