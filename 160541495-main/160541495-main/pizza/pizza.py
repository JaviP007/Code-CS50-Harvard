import tabulate
import csv
import sys
x=sys.argv
if len(x)<=1:
    sys.exit("Too few arguments")
elif len(x)>2:
    sys.exit("Too many arguments")
else:
    x=sys.argv[1]
    if x[-4:]==".csv":
        try:
            pizzas=[]
            with open(x,) as pizza:
                reader = csv.reader(pizza)
                headers = next(reader)
                for row in reader:
                    pizzas.append(row)
                print(tabulate.tabulate(pizzas,headers=headers,tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("No csv")

