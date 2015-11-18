import pickle
verify = input("Really delete all contents? Enter DELETEALL to continue: ")
if verify == "DELETEALL":
    filename = input("File to be wiped: ")
    data = {}
    pickle.dump(data, open(filename, "wb"))
    print("Done.")
else:
    print("Operation cancelled.")
