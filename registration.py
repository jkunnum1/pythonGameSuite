#Register

import verification

import pickle


def register():
    users = pickle.load(open("users.dat", "rb"))
    username = input("Enter a username: ")
    valid = False
    while not valid:
        if username in users:
            print("Invalid username! Try again!")
            valid = False
            username = input("Enter a username: ")
        else:
            valid = True
    match = False
    while not match:
        password = input("Enter a password: ")
        while len(password) < 5:
            print("Please choose a more secure password!")
            password = input("Enter a password: ")
        confirmPassword = input("Confirm password: ")
        if password != confirmPassword:
            print("Passwords don't match!")
        else:
            match = True
    firstName = input("First name: ")
    while firstName == '':
        print("Your first name cannot be blank!")
        firstName = input("First name: ")
    lastName = input("Last name: ")
    while lastName == '':
        print("Your last name cannot be blank!")
        lastName = input("Last name: ")
    email = input("Enter email: ")
    validEmail = verification.emailVerify(email)
    while not validEmail:
        print("Sorry, this email is in invalid format!")
        email = input("Enter email: ")
        validEmail = verification.emailVerify(email)
    age = input("Enter age: ")
    while not age.isdigit():
        print("Sorry, that is not a valid age!")
        age = input("Enter age: ")
    score = 0
    users[username] = [username, password, firstName, lastName, email, age,
                       score]
    pickle.dump(users, open("users.dat", "wb"))

