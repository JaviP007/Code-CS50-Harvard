import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        x = s.split('src="')[1].split('"')[0]
        if None==re.search(r"(^https://www\.youtube\.com/embed/.+$|^http://youtube\.com/embed/.+$|^https://youtube\.com/embed/.+$)",x):
            return None
        else:
            return f"https://youtu.be/{x.split("embed/")[1]}"
    except IndexError:
        None


if __name__ == "__main__":
    main()
