print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth ticket are ${bill}.")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")

    wants_photo = input("Do you want a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")



# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi < 18.5:
#     print("underweight")
# elif 18.5 <= bmi < 25:
#     print("normal weight")
# elif bmi >= 25:
#     print("overweight")
