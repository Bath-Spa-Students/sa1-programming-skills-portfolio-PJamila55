'''( 1 ) Exercise 6 - Brute Force Attack Simulation'''
# Princess Jamila Dinglasan

'''( 2 ) Assigning Variables'''
secret_code = "12345"
peanut_butter = 5
jelly = 0

'''( 3 ) User Input'''
while jelly < peanut_butter:
    entry = input("Enter the password: ")
    
    if entry == secret_code:
        print("Access granted. Welcome back! :)")
        break

    else: # When password is wrong
        jelly += 1
        remaining_attempts = peanut_butter - jelly
        
        if remaining_attempts > 0:
         print(f"Wrong password. You have {remaining_attempts} attempt(s) left.")
        else:
         print("You've reached the maximum number of attempts. Authorities have been notified ⚠️.")

