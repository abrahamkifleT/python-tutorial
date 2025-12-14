

print("Welcome to Treasure Island Your mission is to find the treasure")

user_choose = input("choose left or right? ").lower()

if user_choose == "right":
    print("Game Over")
elif user_choose == "left":
    user_choose = input("Choose Swim or Wait? ").lower()
    if user_choose == "swim":
        print("Game Over!")
    else:
        user_choose = input("Which door Red, Blue, or Yellow? ").lower()
        if user_choose == "red" or user_choose == "blue":
            print("Game Over!")
        else:
            print("You Win!")