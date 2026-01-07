import random

# hard level
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "^", "&", "*", "(", ")", "+"]

print("Welcome to password generator!")
s_letter = int(input("How many letters would you like in your password? \n"))
s_number = int(input("How many numbers would you like in your password? \n"))
s_symbol = int(input("How many symbols would you like in your password? \n"))
password = []
for let in range(0, s_letter):
    password.append(random.choice(letters))
for num in range(0, s_number):
    password.append(random.choice(numbers))
for sym in range(0, s_symbol):
    password.append(random.choice(symbols))
random.shuffle(password)
pas = ""
for ch in password:
    pas += ch
print(pas)
