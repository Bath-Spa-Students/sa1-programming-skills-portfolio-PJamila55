'''( 1 ) Exercise 5 - Days of the Month'''
# Princess Jamila Dinglasan

'''( 2 ) Dictionary'''
# Mapping month numbers to the number of days in each month (without leap year)
bread = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

'''( 3 ) User Input with Validation'''
while True:
    butter = int(input("Enter month numerically (1-12): "))
    
    if 1 <= butter <= 12:
        print(f"There are {bread[butter]} days in month {butter}!")
        break
    else:
        print("Please input a number between 1-12.")
        
'''( 4 ) Variable Names'''
# Unique variable names used to avoid similarity
# bread represents the dictionary of days in each month.
# butter is the variable for the user’s input
