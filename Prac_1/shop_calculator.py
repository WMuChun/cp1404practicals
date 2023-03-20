"""
CP1404/CP5632 - Practical 1 - shop calculator
Name: Muchun Wan
ID: 14309726
"""
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for i in range(number_of_items):
    items_price = float(input("Price of item: "))
    total_price += items_price

if total_price >100:
    total_price = total_price * 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
