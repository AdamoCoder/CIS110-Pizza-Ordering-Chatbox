print("Hello, my name is Adamo your virtual assistant. I will help you order a pizza!")
print("Iam going to ask you a few questions. After typing an answer press enter to continue.")
userName = input("\nEnter your name: ")
print(f"\nHello, {userName}. Nice to meet you!")
input("Press enter to continue . . .")
size = input("\nWhat zise do you want? Enter small, medium, large: ")
flavor = input("\nEnter the flavor of pizza: ")
crustFlavor = input("\nWhat type of crust do you want: ")
quantity = input('\nHow many of this do you want to order? Enter a numeric value: ')
quantity =int(quantity)
method = input('\nIs this carry out or delivery: ')
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost* quantity) * salesTax
print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustFlavor} crust costs ${total}.")
