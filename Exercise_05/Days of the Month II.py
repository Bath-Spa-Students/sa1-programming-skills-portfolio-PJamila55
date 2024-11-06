'''( 1 ) Exercise 5 - Days of the Month - ADVANCED'''
# Princess Jamila Dinglasan

'''( 2 ) Dictionary'''
# Mapping month numbers to the number of days in each month
bread = {
    1: 31,  # January
    2: 28,  # February (leap year adjustable)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

'''( 3 ) Leap Year'''
while True:
    butter = int(input("Enter month numerically (1-12): "))
    
    if 1 <= butter <= 12:
        if butter == 2:
            is_leap = input("Is it a leap year? (yes/no): ").strip().lower()
            
            if is_leap == "yes":
                print("There are 29 days in February during a leap year!")
            else:
                print("There are 28 days in February.")
        else:
            print(f"There are {bread[butter]} days in month {butter}!")
        break
    else:
        print("Please input a number between 1-12.")

'''( 4 ) Variable Names'''
# Unique variable names used to avoid plagiarism
# bread represents the dictionary of days in each month.
# butter is the variable for the user’s input
