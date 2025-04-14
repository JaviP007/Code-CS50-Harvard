while True:
    try:
        x=input("Fraction: ")
        a,b= x.split("/")
        a=int(a)
        b=int(b)
        if b!=0 and a<=b:
            y=(a/b)*100
            y=int(round(y,0))
            if y==100 or y==99:
                print("F")
            elif y==0 or y==1:
                print("E")
            else:
                print(f"{y}%")
        else:
            continue
    except ValueError:
        continue
    else:
        break

