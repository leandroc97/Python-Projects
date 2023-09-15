
# Simple quiz with a few functions and loops to increment user's score.

print("Welcome to my computer quiz!")
# Define a variable for the user's answer.

playing = input("Do you want to play? (yes / no) ")

if playing.lower() != "yes":
    quit()


# Define a variable to store the user's name

name = input("What's your name?")

print("Okay! Let's play, " + name + " :)")
# score value starts at 0
score = 0

# if the user answers correctly, then the score increases by 1 point, else score remains the same.
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
# the lower function is to convert the user's response into lowercase
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Showing the score to the user, in this game the score = number of correct questions
print("You got " + str(score) + " questions correct!")
# Showing the score in %
print("You got " + str((score / 4) * 100) + "%.")
