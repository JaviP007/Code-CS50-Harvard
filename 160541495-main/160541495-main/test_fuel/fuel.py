def main():
    x=input("Fraction: ")
    y=gauge(convert(x))
    print(y)

def convert(fraction):
    try:
        x=fraction
        a,b= x.split("/")
    except (ValueError):
        raise ValueError("Mal")

    a=int(a)
    b=int(b)
    if b==0:
        raise ZeroDivisionError("Division 0")
    elif a>b:
        raise ValueError("a mayor que b")
    else:
        y=(a/b)*100
        y=int(round(y,0))
        return y


def gauge(percentage):
    y=percentage
    if y==100 or y==99:
        return ("F")
    elif y==0 or y==1:
        return ("E")
    else:
        return (f"{y}%")


if __name__ == "__main__":
    main()

