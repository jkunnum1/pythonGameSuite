#Project

import pickle
import LoginGUI

def login():
    users = pickle.load(open("users.dat", "rb"))
    credentials = LoginGUI.LoginGUI(users)
    try:
        username = credentials.getUsername()
        # To save in case a new user was added, we will pickle our updated
        # users dictionary
        user = users[username]
        pickle.dump(user, open("userOnline.dat", "wb"))
    except:
        print("Unexpected Hault!")


login()
