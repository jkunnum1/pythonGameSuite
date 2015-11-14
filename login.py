#Project

import pickle
import quizGenerator

def login():
    users = pickle.load(open("users.dat", "rb"))
    username = input("Username: ")
    password = input("Password: ")
    if username in users:
        if password == users[username][1]:
            user = users[username]
            capitalQuiz(user)
        else:
            print("incorrect username/Password")
    else:
        print("incorrect username/Password")
    print(user)

def capitalQuiz(user):
    print("\nFor the second part of the lab:\n")
    print("QUIZ TIME!\nHope you know your capitals!\n")
    capitals = {"New York": "Albany", "Pennsylvania": "Harrisburg",
                "Michigan": "Lansing", "Maryland": "Annapolis",
                "Florida": "Tallahassee", "Ohio": "Columbus",
                "Texas": "Austin", "New Jersey": "Trenton",
                "Montana": "Helena", "Delaware": "Dover", "Kansas": "Topeka",
                "Connecticut": "Hartford"}
    keys = ["New York", "Pennsylvania", "Michigan", "Maryland", "Florida",
            "Ohio", "Texas", "New Jersey", "Montana", "Delaware",
            "Kansas", "Connecticut"]
    again = 'y'
    correct = 0
    incorrect = 0
    total = 0
    while again == 'y':

        location = quizGenerator.questionPicker(keys)
        answer = input("What is the capital of " + location + "? ")
        if quizGenerator.answerCheck(capitals, location, answer):
            correct += 1
            print("Correct! ", answer, " is the captial of ", location,
                  "!\nYour score is now: ", correct, sep='')
        else:
            incorrect += 1
            print("Sorry, ", answer, " is not the capital of ", location,
                  ".", sep='')

        total += 1
        again = input("Enter 'y' to keep going, or 'e' to exit: ")
        while again != 'y' and again != 'e':
            print("Sorry,", again, "is not a valid option! Try again!")
            again = input("Enter 'y' to keep going, or 'e' to exit: ")

    percent = correct / total * 100
    if percent < 65:
        print("\nYou may want to study up!\nYou got", correct,
              "correct out of a total of", total, "questions!",
              "\nThat's a", format(percent, '.2f'), "percent!")
    elif percent < 100:
        print("\nWell done! You got", correct, "correct out of", total,
              "questions!\nThat's a", percent, "percent!")
    else:
        print("\nOUTSTANDING! You got", correct, "correct out of", total,
              "questions!\nThat's a", percent, "percent! (That's better",
              "than I can ever get!)")
    user[-1] += correct
    print("\n== Goodbye! ==")


login()
