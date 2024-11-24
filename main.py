import random
import string


def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 8:
            print("It's recommended to use at least 8 characters for a strong password.")

        password = generate_password(length)

        print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")


if __name__ == "__main__":
    main()