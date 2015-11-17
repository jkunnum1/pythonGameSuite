#Project

import pickle
import LoginGUI

def login():
    users = pickle.load(open("users.dat", "rb"))
    credentials = LoginGUI.LoginGUI(users)
    try:
        username = credentials.getUsername()
        #users = credentials.getUsers()
        # To save in case a new user was added, we will pickle our updated
        # users dictionary
        user = users[username]
        print(user[2], user[3], "just logged in as", user[0])
    except:
        print("Unexpected Hault!")


login()
