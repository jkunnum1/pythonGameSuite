#Project
# William McLaughlin
# A 51
# S. Douglas Wehbe
# A 52
# Julie Kunnumpurath
# A 53
# John Henry Burns
# A 52
# Rebecca Trackman
# A 52


import pickle
import LoginGUI
import MainMenuGUI


def login():
    users = pickle.load(open("users.dat", "rb"))
    credentials = LoginGUI.LoginGUI(users)
    try:
        username = credentials.getUsername()
        if username != '':
            # To save in case a new user was added, we will pickle our updated
            # users dictionary
            user = users[username]
            pickle.dump(user, open("userOnline.dat", "wb"))
            menu = MainMenuGUI.MyGUI()
            userOnline = []
            pickle.dump(userOnline, open("userOnline.dat", "wb"))

    except:
        print("Unexpected Hault!")


login()
