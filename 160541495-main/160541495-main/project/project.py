import sys

def main():
    sistema()

def sex():
    while True:
        try:
            sis= int(input("Select: \n1-Male\n2-Female\n"))
            if sis !=1 and sis !=2:
                print("You have to select 1 or 2")
                continue
            else:
                return sis
        except ValueError:
            print("You have to select 1 or 2, no letters are accepted")
            pass

def age():
    while True:
        try:
            edad= int(input("What is your age: "))
            if edad <18:
                sys.exit("You are to young to take the test, the minimum age is 18 years")
            elif edad > 100:
                sys.exit("You are to old to take the test, the maximun age is 100 years")
            else:
                return edad
        except ValueError:
            pass

def sistema():
    while True:
        try:
            sis= int(input("Select: \n1-Metric system\n2-Imperial system\n"))
            if sis !=1 and sis !=2:
                print("You have to select 1 or 2 to choose your system of measurement")
                continue
            else:
                return sis
        except ValueError:
            print("You have to select 1 or 2 to choose your system of measurement, no letters are accepted")
            pass

def heigh():
    while True:
        try:
            altura= int(input("What is your heigh: "))
            if altura <18:
                sys.exit("Enter a valid heigh")
            elif altura > 100:
                sys.exit("Enter a valid heigh")
            else:
                return altura
        except ValueError:
            pass

def weigh():
    ...

def sleep():
    ...

def activity():
    ...

def smoking():
    ...

def drinking():
    ...


if __name__ == "__main__":
    main()
