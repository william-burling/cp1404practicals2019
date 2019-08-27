MIN_LENGTH = 1
MAX_LENGTH = 10
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    password = get_valid_password()
    censor_password(password)


def get_valid_password():
    password = input("password: ")
    while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        password = input("invalid password please enter another: ")
    return password


def censor_password(password):
    for char in password:
        print("*", end="")


main()
