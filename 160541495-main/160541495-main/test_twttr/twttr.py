def main():
    x=input()
    x=shorten(x)
    print(x)


def shorten(word):

    vowels = "aeiouAEIOU"
    for i in vowels:
        word=word.replace(i,"")
    return word

if __name__ == "__main__":
    main()
