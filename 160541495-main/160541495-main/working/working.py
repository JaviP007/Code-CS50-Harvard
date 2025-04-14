import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        x = s
        if None==re.search(r"(^([0-9]|1[0-2]):([0-5][0-9]) (AM|PM) to ([0-9]|1[0-2]):([0-5][0-9]) (AM|PM)$|^([0-9]|1[0-2]) (AM|PM) to ([0-9]|1[0-2]) (AM|PM)$)",x):
            raise ValueError("Mal")
        else:
            if ":" not in x:
                start,end=x.split(" to ")
                x= f"{start.split(" ")[0]}:00 {start.split(" ")[1]} to {end.split(" ")[0]}:00 {end.split(" ")[1]}"
                start,end = x.split(" to ")
                if "AM" in start and "12:" in start and "AM" in end and "12:"in end :
                    return f"00:{start.split(":")[1].split(" ")[0].zfill(2)} to 00:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "AM" in start and "12:" in start and "PM" in end and "12:"in end :
                    return f"00:{start.split(":")[1].split(" ")[0].zfill(2)} to 12:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "AM" in start and ":" in start and "AM" in end and ":"in end :
                    return f"{start.split(":")[0].zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {end.split(":")[0].zfill(2)}:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "AM" in start and ":" in start and "PM" in end and ":"in end :
                    return f"{start.split(":")[0].zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {str(int(end.split(":")[0])+12).zfill(2)}:{end.split(":")[1].split(" ")[0]}".strip()
                elif "PM" in start and ":" in start and "PM" in end and ":"in end :
                    return f"{str(int(start.split(":")[0])+12).zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {str(int(end.split(":")[0])+12).zfill(2)}:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "PM" in start and ":" in start and "AM" in end and ":"in end :
                    return f"{str(int(start.split(":")[0])+12).zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {str(int(end.split(":")[0])).zfill(2)}:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()

            else:
                start,end = x.split(" to ")
                if "AM" in start and "12:" in start and "AM" in end and "12:"in end :
                    return f"00:{start.split(":")[1].split(" ")[0].zfill(2)} to 00:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "AM" in start and "12:" in start and "PM" in end and "12:"in end :
                    return f"00:{start.split(":")[1].split(" ")[0].zfill(2)} to 12:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "AM" in start and ":" in start and "AM" in end and ":"in end :
                    return f"{start.split(":")[0].zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {end.split(":")[0].zfill(2)}:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "AM" in start and ":" in start and "PM" in end and ":"in end :
                    return f"{start.split(":")[0].zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {str(int(end.split(":")[0])+12).zfill(2)}:{end.split(":")[1].split(" ")[0]}".strip()
                elif "PM" in start and ":" in start and "PM" in end and ":"in end :
                    return f"{str(int(start.split(":")[0])+12).zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {str(int(end.split(":")[0])+12).zfill(2)}:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()
                elif "PM" in start and ":" in start and "AM" in end and ":"in end :
                    return f"{str(int(start.split(":")[0])+12).zfill(2)}:{start.split(":")[1].split(" ")[0].zfill(2)} to {str(int(end.split(":")[0])).zfill(2)}:{end.split(":")[1].split(" ")[0].zfill(2)}".strip()


    except IndexError:
        None

if __name__ == "__main__":
    main()
