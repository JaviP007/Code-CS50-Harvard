x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

try:
    if int(x)== 42:
        print("Yes")
    else:
        print("No")
except ValueError:
    x = x.strip().lower()
    if x=="forty two" or x=="forty-two":
        print("Yes")
    else:
        print("No")
