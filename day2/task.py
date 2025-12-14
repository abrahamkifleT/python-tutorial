print("Welcome to the Tip Calculator")

total_bill = int(input("what was the total bill ? "
                   ))
how_much_tip_to_give = int(input("How much tip would you like to give? 10, 12, or 15? "))

how_many_people_to_split = int(input("How many people to split the bill? "))


how_much_tip_to_give_perPerson = how_much_tip_to_give / 100 + 1
total_bill_after_tip = how_much_tip_to_give_perPerson * total_bill

print(round(total_bill_after_tip / how_many_people_to_split, 2))