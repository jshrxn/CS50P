from validator_collection import validators, errors

def main():
    email = input("What's your email address? ")
    print(validate(email))

def validate(z):
    try:
        validators.email(z)
        return "Valid"

    except errors.EmptyValueError:
        return "Invalid"

    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()
