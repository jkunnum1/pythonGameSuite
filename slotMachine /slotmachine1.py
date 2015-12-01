# Project

import random
print("Welcome to the Slot Machine Simulator. You start with $20. Each \
game costs $5 to play.")
print('\n')

def askPlayer():
    playGame = input("Would you like to play?")
    score = 20
    while playGame == 'y':
        print('\n')
        if playGame == 'y':
            score -= 5
            print("The three numbers are:")
            first = spinWheel()
            second = spinWheel()
            third = spinWheel()
            score = addScore(score, first, second, third)
        elif playGame == 'n':
            print("Game over! You earned $", addScore)
        else:
            print("wrong input!")
        playGame = input("Would you like to play again?")
    print("Game over! You earned $", score)

def addScore(score, firstWheel, secondWheel, thirdWheel):
    if firstWheel == secondWheel:
        score += 10
    if firstWheel == thirdWheel:
        score += 10
    if secondWheel == thirdWheel:
        score += 10
    if firstWheel == secondWheel and firstWheel == thirdWheel:
        score += 50
    print("You have $", score, "left")
    print('\n')
    return score
    
def spinWheel():
    # returns a random number from the wheel
    randomNumber = random.randint(0, 5)
    print(randomNumber)
    return randomNumber

def main():
    askPlayer()

main()
