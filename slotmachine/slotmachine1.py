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









def main():
    gameOver = False
    play = welcomeLoop("Welcome to The Slot Machines!")
    while not gameOver:
        score = 0
        while play:
            spins = gameLoop(score)
            originalScore = score
            score = addScore(score, spins[0], spins[1], spins[2])
            if score < 0:
                if welcomeLoop("Game Over! Play again?"):
                    play = False
                else:
                    play = False
                    gameOver = True
            elif score > originalScore:
                if not endGame("You Won!", score):
                    play = False
                    gameOver = True
            else:
                if not endGame("You Lost!", score):
                    play = False
                    gameOver = True
