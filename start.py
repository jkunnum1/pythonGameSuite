# Project
# Kunnumpurath, Julie
# A 53
# McLaughlin, William
# A 51
# Wehbe, Semaan
# A 52
# Burns, John Henry
# A 52
# Trackman, Rebecca
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
