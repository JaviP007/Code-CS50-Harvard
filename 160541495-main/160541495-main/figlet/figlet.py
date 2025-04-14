import sys
from pyfiglet import Figlet
x=" ".join(sys.argv[1:])
figlet=Figlet()
j=figlet.getFonts()
if x.split(" ")[0] == "-f" or x.split(" ")[0] =="--font" and x.split(" ")[1] in j:
    x= x.split(" ")[1]
    f=Figlet(font=x)
    t=input("Input: ")
    print(f.renderText(t))
else:
    sys.exit("Invalid usage")
