import pickle
verify = input("Really delete all users? Enter DELETEALL to continue: ")
if verify == "DELETEALL":
    users = {}
    pickle.dump(users, open("users.dat", "wb"))
    print("Done.")
else:
    print("Operation cancelled.")
