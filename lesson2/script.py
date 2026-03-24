print("Welcome to the calculator")
bill = float(input("Please enter the total bill: "))
percent = float(input("How much tip would you like to give: "))
persons = float(input("How many people to split the bill: "))
extra_money = percent / 100 * bill
total_amount = bill + extra_money
print(total_amount)
each_pay = total_amount / persons
print(round(each_pay,2))

