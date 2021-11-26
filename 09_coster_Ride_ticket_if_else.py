# 1. Start
# 2. Height should be > 120 cm to ride
# 3. Age < 12 : $5
# 4. Age = 12-18 : $7
# 5. Age > 18 : $12
# 6. Photos : $3
# 7. Total Bill

print("Hi Welcome to the Great Amusement park.")
height = float(input("Enter your height in cm: "))
bill = 0
if height > 120:
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    photo = input("Do you want to take photo? Press Y or N: ")
    if photo == 'Y':
        bill += 3
        print(f"Your total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")
else:
    print("You are too short to ride")
