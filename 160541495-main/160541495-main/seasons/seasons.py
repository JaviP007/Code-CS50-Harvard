from datetime import date
import inflect
import re
import sys

def main():
    variable=input("Text: ")
    print(getminutesxd(variable))

def getminutesxd(s):

    if None == re.search(r"^\d\d\d\d-(0[1-9]|1[0-2])-\d\d$",s):
        return sys.exit("Invalid date")
    else:
        y,m,d=s.split("-")
        y=int(y)
        m=int(m)
        d=int(d)
        born=date(y,m,d)
        today=date.today()
        difference=today-born
        total_minutes = int(difference.total_seconds() / 60)
        p = inflect.engine()
        str=f"{p.number_to_words(total_minutes,andword='')} minutes"
        words = str.split()
        words[0] = words[0].capitalize()
        str = ' '.join(words)
        return str

if __name__ == "__main__":
    main()
