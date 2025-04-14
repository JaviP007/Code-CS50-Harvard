from validator_collection import validators, checkers, errors
x=input("email: ")
try:
    if x == validators.email(x):
        print("Valid")
    else:
        print("Invalid")
except ValueError:
    print("Invalid")

