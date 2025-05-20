print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name + ",", "you are", age, "years old.")

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    # Can use ".lower()" or ".upper()" to change the input below to upper/lower case regardless of what the user enters.
    if wants_to_play == 'yes':
        print("Let's play!")

        health = 10
        print("You are starting with", health, "health.")

        left_or_right = input("First choice...Left or Right? (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path & reach a lake... Do you swim across or go around? (across/around)? ").lower()

            if ans == "around":
                print("You went around & reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across but were bitten by a fish and lost 5 health")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to? (house/river)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health & lose the game...")
                else:
                    print("You have survived...You win!")
            else:
                print("You fell into the river and lost...")
        else:
            print("You fell of a cliff & lost...")
    else:
        print("Bye.")
#elif age >= 14:
        #print("You can play with adult supervision")
else:
    print("You are not old enough to play.")


''''
"elif" is used after "if" and multiple can be used but the last must always be "else".
It's shown here for educational purpose.
'''