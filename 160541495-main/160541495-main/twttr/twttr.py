def main():
    x=input()
    shorten(x)


def shorten(word):

    vowels = "aeiouAEIOU"
    for i in vowels:
        word=word.replace(i,"")
    print(f"Output: {word}")

if __name__ == "__main__":
    main()



