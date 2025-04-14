import random

def main():
    a=0

    level=get_level()

    for _ in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        b=0
        while b <3:
            try:
                z=int(input(f"{x} + {y} ="))
            except ValueError:
                b=b+1
                print("EEE")
                continue
            if z!=x+y:
                b=b+1
                print("EEE")
            else:
                a=a+1
                break
        if b==3:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {int(a)}")













def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x==1 or x==2 or x==3:
                return int(x)
            else:
                continue
        except ValueError:
             continue

def generate_integer(level):
    if level == 1:
            x=random.randint(0,9)
            return x
    elif level==2:
            x=random.randint(10,99)
            return x
    elif level==3:
            x=random.randint(100,999)
            return x
    else:
        raise ValueError("Mal")

if __name__ == "__main__":
    main()

