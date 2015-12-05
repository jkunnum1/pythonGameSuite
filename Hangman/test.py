import pickle

highScores = pickle.load(open("hangmanScores.dat", "rb"))
print(highScores)