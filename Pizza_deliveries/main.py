print("Welcome tp python pizza deliveries")
size = input("what size do you want? s, m or l: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N : ")
extra_cheese = input("Do you want extra cheese on you pizza? Y or N : ")
small = 15
medium = 20
large = 25
total_bill = 0
if size == "s":
    total_bill += small
    if pepperoni == "Y":
        total_bill += 2
    if extra_cheese == "Y":
        total_bill += 1
    print("Your total bill is $", total_bill)
elif size == "m":
    total_bill += medium
    if pepperoni == "Y":
        total_bill += 3
    if extra_cheese == "Y":
        total_bill += 1
    print("Your total bill is $", total_bill)
elif size == "l":
    total_bill += large
    if pepperoni == "Y":
        total_bill += 3
    if extra_cheese == "Y":
        total_bill += 1
    print("Your total bill is $", total_bill)
