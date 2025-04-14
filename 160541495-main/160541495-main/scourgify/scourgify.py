import csv
import sys
x=sys.argv

if len(x)<=2:
    sys.exit("Too few arguments")
elif len(x)>3:
    sys.exit("Too many arguments")
else:
    x=sys.argv[1]
    if x[-4:]==".csv":
        try:
            after1=[]
            after2=[]
            with open(x,) as before:
                reader = csv.reader(before)
                headers = next(reader)
                for row in reader:
                    after2.append(row[0].split(","))
                    after1.append(row[1])

                after=list(zip(after1,after2))
                head=["first","last","house"]
                split_list = [[name[1].strip(), name[0],house] for house, name in after]
                final=split_list
                with open(sys.argv[2], 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(head)
                    for row in final:
                        writer.writerow(row)
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("No csv")


