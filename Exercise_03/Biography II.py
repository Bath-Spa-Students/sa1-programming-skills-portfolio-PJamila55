'''( 1 ) Exercise 3 - Biography - ADVANCED'''
# Princess Jamila Dinglasan

'''( 2 ) Variables'''
# Ask the user to type their information and store it in the variable
name = input("What is your name? ")
hometown = input("What is your hometown? ")

while True:
    age = input("How old are you? ")
    if age.isdigit(): # Accepts if the user's "age" is typed as an integer or digit
        age = int(age) 
        break 
    else:
        print("Please enter it in digits. ") # Forces the user to type in their age properly before continuing

'''( 3 ) Print Dictionary'''
print("Your Information:")

# Store the information in a dictionary with keys for each input
user_info = {
    'name': name,
    'hometown': hometown,
    'age': age
}

# Prints everything in one line
print(f"Name: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}")
