import string
import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if any(char in string.punctuation for char in s):
        return False
    else:
        if any(char.isdigit() for char in s):
            if s[-1].isdigit()==True and 2<=len(s)<=6 and s[:2].isalpha()==True and s.isspace()!=True and s.split("0")[0].isalpha()!=True and s.split() and re.split("\d+",s)[1]=="":
                return True
            else:
                return False #ojo no te olvides de este else de este if
        else:
            if s[:2].isalpha()==True and 2<=len(s)<=6 and s.isspace()!=True:
                return True
            else:
                return False

if __name__ == "__main__":
    main()

