import random
import time

rand = random.randint(0, 3)

words = ["wisdom", "ariana grande", "xylophone", "sishacomapa"]
word = words[rand]

gotten = []
guesses = []

nop = int(input("How many players are playing: "))

print()
print("WE BEGIN!!!!")

continue_code = 1

player_scores = []
for i in range(nop):
    player_scores.append(0)

while continue_code:
    count = 0
    print()
    for i in range(len(word)):
        if i in gotten:
            print(word[i], end=" ")
        elif word[i] == " ":
            print(" ", end=" ")
        else:
            print("_", end=" ")
    print()
    guess = input("Guess a letter: ")
    guess = guess.lower()
    prev_len = len(gotten)
    if guess in guesses:
        print("Someone has guessed it already")
    else:
        for i in range(len(word)):
            if guess == word[i]:
                gotten.append(i)
            else:
                pass
        guesses.append(guess)
    new_len = len(gotten)
    points = (new_len-prev_len)*10
    if new_len == prev_len:
        print("Sorry")
    else:
        print("Correct, you have "+ str(points)+" points")
    player_scores[count] += points
    count = (count+1)% nop
    if len(gotten) == len(word):
        continue_code = 0
    print("Next player")

print("NOW FOR THE RESULTS!!!")
print()
time.sleep(1)
for i in range(nop):
    print("Player "+ str(i+1)+ "had: ", end="")
    time.sleep(1)
    print(player_scores[i])
    time.sleep(1)

