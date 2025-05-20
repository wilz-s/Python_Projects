print("Welcome to my computer quiz!")

play = input("Do you want to play? ").lower()
'''
Note that ".lower()" can be placed differently. Can be added alongside the variable to be printed but not at the original name.
e.g. "play" variable can be called "play.lower()"
'''
if play != "yes":
    quit()
    # "quit" function terminates the program. No need for else statement.
print("Okay! Let's play! :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question(s) correct!")
'''
"str()" changes "score" which is a number(an integer in python) to a string(texts in python).
Other way to do it would be add quotations to "score" variable. BUt that would change the variable to plain text.
On the other hand, if the number isn't stored in a variable, you can simply put quotations around the digit(s)
'''

print("You got " + str((score/4) * 100) + "%.")
# If you change the no. of questions, "4" changes.

