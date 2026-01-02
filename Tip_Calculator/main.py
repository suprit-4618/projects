print("Welcome to the Tip Calculator")

total_bill = float(input("What was the total bill? : "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 : "))
split_bill = int(input("How many people to split the bill? : "))

tip_amount = total_bill * (tip / 100)
bill_after_tip = total_bill + tip_amount
individual_pay = bill_after_tip / split_bill

print(f"Each person should pay: {individual_pay:.2f}")
