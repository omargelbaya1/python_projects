print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
tip_given= bill * (tip / 100)
people = int(input("How many people to split the bill? "))

total_bill_paid_per_person=(tip_given + bill)/people

answer=(round(total_bill_paid_per_person, 2))

print(f"Each person should pay ${answer}")
print("testing")
