import random

top_of_range = input("Type a number to set guess range: ")

if top_of_range.isdigit():
# We need to make sure the input is a digit. We check that with ".isdigit()" function.
    top_of_range = int(top_of_range)
# Whatever the user types will come out in quotations. Python reads that as a string, not an integer.
# We use the "int()" function to convert input to an integer. e.g. int("25") -> 25. Note entering a text will give you an error.
    if top_of_range <= 0:
# This doesn't work cos when I input a negative number the '-' is taken as a string triggering the '.isdigit()' function.
# The tutorial video isn't over so let's see if the problem is noticed. If not, leave a comment in the video.
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a digit next time.")
    quit()

random_number = random.randint(0,top_of_range)
# "randint" is used to generate numbers between the start(in this case 0) & stop(user input "top_of_range").
guesses = 0

# random_number = (random.randrange(-5,11))
'''
'randrange' like 'randint' is used to generate numbers between the start & stop. Noted above is an example.
Difference that the stop value will not be generated, just the number before it(in this case 10). 
Also if range starts at 0, no need to input it as start value. Can only add stop value.
'''
while True:
    ''' 
"while" is "While loop". It means whatever program that comes after will run if the the condition(previous program above) is "True".
 It is ended with "break" keyword which will be shown below otherwise it'll run infinitely. The while loop could also be used as:
    while user_guess(new variable) != random_number:
we don't for the purpose of learning about "break"
'''
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a digit next time.")
        continue
        # this brings us back to the top of the loop.

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses.")
# with ',' you don't need to add space within the colons or change the guess variable to a string with string function.
# Note that you could add the guesses variable with "you got it!" above the break. Instead of printing extra lines & writing more code.

