Frutas=["Apple","Avocado","Banana","Cantaloupe","Grapefruit","Grapes","Honeydew Melon","Kiwifruit","Lemon","Lime","Nectarine","Orange","Peach","Pear","Pineapple","Plums","Strawberries","Sweet Cherries","Tangerine","Watermelon"]
Calorias=[130,50,110,50,60,90,50,90,15,20,60,80,60,100,50,70,50,100,50,80]

fruits={Frutas[i]:Calorias[i] for i in range(len(Frutas))}

x=input("Item: ")
if len(x.split())==2:
    a,y=x.split()
    a=a.capitalize()
    y=y.capitalize()
    x=a+" "+y
else:
    x=x.capitalize()
    x=x.strip()
if x in fruits:
    print(f"Calorias: {fruits[x]}")
else:
    print("")
