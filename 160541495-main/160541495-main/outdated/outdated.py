import string
l=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
m=list(range(1,13))
n={l[i]:m[i] for i in range(len(l))}


while True:
    x=input("Date: ")
    if any(char.isalpha()for char in x) and len(x.split(" "))==3 and x.strip().split(" ")[0].isalpha()==True and "," in x and int(x.translate(str.maketrans('', '', string.punctuation)).strip().split(" ")[1])<=12:
        x = x.translate(str.maketrans('', '', string.punctuation)).strip()
        a,y,z= x.split(" ")
        print(f"{int(z)}-{int(n[a]):02}-{int(y):02}",end="")
        break
    elif all(a.isdigit() for a in x.strip().split("/")):
        if len(x.split("/"))==3 and int(x.split("/")[0])<=12 and int(x.split("/")[1])<=31 and x.strip().split("/")[1].isdigit() and x.strip().split("/")[0].isdigit() and x.strip().split("/")[2].isdigit():
            x=x.strip()
            a,y,z=x.split("/")
            print(f"{int(z)}-{int(a):02}-{int(y):02}",end="")
            break
        else:
            continue
    else:
        continue

