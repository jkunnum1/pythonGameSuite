# Project
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
verify = input("Really delete all contents? Enter DELETEALL to continue: ")
if verify == "DELETEALL":
    filename = input("File to be wiped: ")
    data = {}
    pickle.dump(data, open(filename, "wb"))
    print("Done.")
else:
    print("Operation cancelled.")

