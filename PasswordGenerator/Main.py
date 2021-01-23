import random
import sys
import json

def generate_password(length):
    small_alpha = "abcdefghijklmnopqrstuvwxyz"
    big_alpha = small_alpha.upper()
    numbers = "01234456789"
    special_chrs = "!@#$$%^&*()"
    characters =  small_alpha+big_alpha+numbers+special_chrs
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def generate_password2():
    with open("./PasswordGenerator/random_words.json", "r") as f:
        words = f.read()

    words = json.loads(words)

    numbers =  "01234456789"
    special_chrs = "!@#$$%^&*()"
    all_chrs = numbers+special_chrs
    password = ""
    password += random.choice(words)
    password += random.choice(numbers)
    password += random.choice(all_chrs)
    password += random.choice(special_chrs)
    password += random.choice(words)

    return password
    


if __name__=="__main__":
    pass_type = sys.argv[1]
    if pass_type == "a":
        length = int(sys.argv[2])
        password = generate_password(length)
        print(password)
    elif pass_type == "b":
        password = generate_password2()
        print(password)
    else:
        print("Argument input should be 'a' or 'b'")

    