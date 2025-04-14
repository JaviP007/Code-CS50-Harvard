x=input("variable ")

for i in range(len(x)):
    if (x[i].isupper())==True:
        x=x.replace(x[i],"_"+x[i].lower())
    else:
        x=x
print(x)
