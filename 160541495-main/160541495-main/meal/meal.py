def main():
    a = input("Que hora es: ")
    x=convert(a)
    if 7<=x<=8:
        print("breakfast time")
    elif 12<=x<=13:
        print("lunch time")
    elif 18<=x<=19:
        print("dinner time")

def convert(time):
    a,b = time.split(":")
    x= int(a)+(int(b)/60)
    return x


if __name__ == "__main__":
    main()
