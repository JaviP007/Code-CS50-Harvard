import inflect
p = inflect.engine()
l=[]
try:
    while True:
        x=input("")
        l.append(x)
        mylist = p.join((l), final_sep=",")
except EOFError:
    print(f"Adieu, adieu, to {mylist}")
    pass
