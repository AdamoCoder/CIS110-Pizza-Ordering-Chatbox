print("Hello, my name is Adamo your virtual assistant. I will help you order a pizza!")

print("Iam going to ask you a few questions. After typing an answer press enter to continue.")

userName = input("\nEnter your name: ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name: ")
if userName.lower() == "adamo":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Pleasure to serve you!")

input("Press enter to continue . . .")

size = input("\nWhat zise do you want? Enter small, medium, large: ")
if size == "small":
    pizzaCost = 8.99
elif size == "medium":
    pizzaCost = 12.99
elif size == "large":
    pizzaCost = 14.99
else:
    print("Invalid size entered. Defaulting to medium.")
    pizzaCost = 12.99
    size = "medium"

flavor = input("\nEnter the flavor of pizza: ")
while len(flavor) == 0:
    flavor = input("Flavor cannot be blank! Please enter your flavor: ")

crustFlavor = input("\nWhat type of crust do you want: ")
while len(crustFlavor) == 0:
    crustFlavor = input("Crust type cannot be blank! Please enter a flavor.")

quantity = input('\nHow many of this do you want to order? Enter a numeric value: ')
while not quantity.isdigit():
    quantity = input("\nValue not recognized. Please enter a numeric value: ")
quantity =int(quantity)

method = input('\nIs this carry out or delivery: ')
while method == 0:
    method = input("Invalid value! Please enter carry out or delivery: ")
if method == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

salesTax = 1.1


total = (pizzaCost* quantity) * salesTax + deliveryFee

print("-" * 10)

print(f"Thank you, {userName}, for your order.")

print(f"Your {quantity} {size} {flavor} pizza(s) with {crustFlavor} crust costs ${total}.")

if total >= 50:
    print("\nCongratulations! You've been awarded a $10 off coupon!")
else:
    print("\nOrder over $50 will receive a free $10 off coupon!")

print("-" * 10)

