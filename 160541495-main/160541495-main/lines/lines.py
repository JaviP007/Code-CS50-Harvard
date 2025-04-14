import sys
a=0
x= sys.argv

if len(x)<=1:
    sys.exit("Too few arguments")
elif len(x)>2:
    sys.exit("Too many arguments")
else:
    x=sys.argv[1]
    if x[-3:]==".py":
        try:
            with open(x) as file:
                for line in file:
                    if line!="\n" and line.strip() !="" and line.strip()[0]!="#" :
                        a=a+1
                    else:
                        a=a
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("No py")
print(a)
