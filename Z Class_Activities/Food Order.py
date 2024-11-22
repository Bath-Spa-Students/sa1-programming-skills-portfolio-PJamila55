'''Taking a Food Order'''

def get_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ["yes", "no"]:
            return response
        print("Please answer with 'yes' or 'no'.")

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_confirm_cancel(prompt):
    while True:
        response = input(prompt).lower()
        if response in ["confirm", "cancel"]:
            return response
        print("Please answer with 'confirm' or 'cancel'.")

# Main program
food = input("What would you like to order? : ")
print(food)

answer = get_yes_no(f"Is {food} your favorite? ")
print("Okay")

buy = get_integer(f"How many {food} would you like to buy? ")
print(f"{buy} ?")
print("Okay")

final = get_yes_no(f"Are you sure you want to buy {buy} orders of {food}? ")
print("Okay, great!")

answ = get_yes_no("Do you want anything else? (yes/no) ")

if answ == "no":
    print(f"Okay, thanks! your {buy} orders of {food} will be delivered shortly...")
elif answ == "yes":
    extra = input("What would you like to add? ")
    another = get_confirm_cancel(f"An order of {extra} will be added. (confirm/cancel) ")
    if another == "confirm":
        print(f"Your {buy} orders of {food} and another order of {extra} will be delivered shortly...")
    elif another == "cancel":
        print(f"Alright, your {buy} orders of {food} will be delivered shortly...")
