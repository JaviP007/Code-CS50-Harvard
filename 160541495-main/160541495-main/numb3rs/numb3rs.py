import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if None == re.search(
        r"^([0-9]|\d\d|1\d\d|2[0-4][0-9]|2[0-5][0-5])\.([0-9]|\d\d|1\d\d|2[0-4][0-9]|2[0-5][0-5])\.([0-9]|\d\d|1\d\d|2[0-4][0-9]|2[0-5][0-5])\.([0-9]|\d\d|1\d\d|2[0-4][0-9]|2[0-5][0-5])$",
        ip,
    ):
        return False
    else:
        return True


if __name__ == "__main__":
    main()
