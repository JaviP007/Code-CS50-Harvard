def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    try:
        return(float(d))
    except ValueError:
        d=d.replace("$","")
        return(float(d))


def percent_to_float(p):
    try:
        return(float(p))
    except ValueError:
        p=p.replace("%","")
        return(float(int(p)/100))
main()
