x=input("greeting ")
x=x.strip()

print(x)

if x[0:5]=="Hello":
    print("$0")
elif x[0]=="H":
    print("$20")
else:
    print("$100")

