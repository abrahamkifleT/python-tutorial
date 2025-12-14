
import random


user_choose = int(input("what is you choose? Type 0 for Rock, 1 for paper, 2 for Scissors. "))
computer_choose = random.randint(0,2)
print("User Choose", user_choose)
print("Computer Choose", computer_choose)
if user_choose == 0 and computer_choose == 2 or user_choose == 1 and computer_choose == 0 or user_choose == 2 and computer_choose == 1:
    print("User win")    
elif computer_choose == 0 and user_choose == 2 or computer_choose == 1 and user_choose == 0 or computer_choose == 2 and user_choose == 1:
    print("Computer win")
else:
    print("draw")
    
    