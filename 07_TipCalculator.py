# This code will calculate the Bill and split.

bill_value = float(input("Hi, Enter the Bill value: "))
tip_pcent = float(input("Enter Tip percent: "))
bill_split = int(input("How many people are splitting the bill?: "))

net_bill = (bill_value + (bill_value / 100) * tip_pcent) / bill_split

print(f"Each person should pay Rupees {round(net_bill, 2)}.")
