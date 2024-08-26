# This a password Generator using "Python" it's a open-source project
# Devloped by Gowshik.
# Linkedin - Gowshik Anbu : www.linkedin.com/in/gowshik-anbu-1123382b1
# Instagram - @igowshikofficial : https://www.instagram.com/igowshikofficial/
# Github - https://github.com/Gowshikgit
# Gmail - gowshikofficia18@gmail.com
# Thank you

# Use 'random' module for random characters in the password.
import random

# print intro.
print('Welcome to "PassGen" make your password Hard to crack')

print("You can make unlimited characters length of password")

print("Most Websites & Applications password length: 64 characters") 

print("Windows password length: 127 characters")

print("Linux/unix systems password length: 255 characters") 

# Number of Lettrs, Number & Symbols to make a characters Password.
lettrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
         ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '`', '<', '>', ',', '.', ';', ':', '/', '?', '"', '|' ]

# User input for how many characters of Lettrs, Number & Symbols in the password. Using while loo to repeat the user input. user wrongly enter string input function will be repeated.
while True:
    try:
        n_lettrs = int(input("Enter how many characters of 'Lettrs' in the password: "))

        if n_lettrs <= 0 :
            print('Not vaild')
            continue

        # If input are valid, break out of the loop
        break

    except ValueError:
        print("Invalid input. Please enter valid number.")

while True:
    try:

        n_numbers = int(input("Enter how many characters of 'Numbers' in the password: "))


        if n_numbers <= 0 :
            print('Not vaild')
            continue


        # If input are valid, break out of the loop
        break

    except ValueError:
        print("Invalid input. Please enter valid number.")

while True:
    try:
        n_symbols = int(input("Enter how many characters of 'Symbols' in the password: "))

        if n_symbols <= 0 :
            print('Not vaild')
            continue

        # If input are valid, break out of the loop
        break

    except ValueError:
        print("Invalid input. Please enter valid number.")
      

# Create a empty variable to store the Generated password in list type.
password_list = []

# Use for loop function to create random characters.

# For lettrs.
for l in range(0,n_lettrs):
    character = random.choice(lettrs)
    password_list += character

# For symbols.
for s in range(0,n_symbols):
    character = random.choice(symbols)
    password_list += character

# For numbers.
for n in range(0,n_numbers):
    character = random.choice(numbers)
    password_list += character

# Create a empty variable to store the Generated password as string.
password = ""

# Use 'random' module to shuffle the password
random.shuffle(password_list)

# For loop function to list into string
for character in password_list:
    password += character

# Finaly print the password. 
print('Your Password: ', password)
