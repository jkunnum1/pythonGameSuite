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
verify = input("Really delete all contents? Enter DELETEALL to continue: ")
if verify == "DELETEALL":
    filename = input("File to be wiped: ")
    data = {}
    pickle.dump(data, open(filename, "wb"))
    print("Done.")
else:
    print("Operation cancelled.")

