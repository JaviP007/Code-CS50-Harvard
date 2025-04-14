def main():
    x=input("greeting: ")
    x=value(x)
    print(x)


def value(greeting):
        greeting=str(greeting).strip().title()
        if greeting[0:5]=="Hello":
            x=0
        elif greeting[0]=="H":
            x=20
        else:
            x=100
        return x



if __name__ == "__main__":
    main()


