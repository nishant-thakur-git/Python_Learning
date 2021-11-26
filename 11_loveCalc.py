# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_string = (name1+name2)
lower_String = combined_string.lower()

t = lower_String.count("t")
r = lower_String.count("r")
u = lower_String.count("u")
e = lower_String.count("e")

true = t + r + u + e

l = lower_String.count("l")
o = lower_String.count("o")
v = lower_String.count("v")
e = lower_String.count("e")

love = l + o + v + e

score = str(true) + str(love)
if 10 > int(score) or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


