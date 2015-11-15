#Project

import pickle
import LoginGUI

def login():
    users = pickle.load(open("users.dat", "rb"))
    credentials = LoginGUI.LoginGUI(users)
    username = credentials.getUsername()
    user = users[username]
    print(user)


login()
