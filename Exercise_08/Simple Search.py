'''( 1 ) Exercise 8 - Simple Search'''
# Princess Jamila Dinglasan

'''( 2 ) Creating Dictionary'''
people = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

'''( 3 ) Asking the User'''
initial_search = input("Would you like to search for Sam? (yes/no): ").strip().lower()

if initial_search == "yes":
    print("Searching...")
    search_term = "sam"
else:
    search_term = input("Who would you like to look for? ").strip().lower()

'''( 4 ) If - Else Statement'''
if search_term in [name.lower() for name in people]:
    print(f"{search_term.capitalize()} is in the list!")
else:
    print(f"{search_term.capitalize()} is not on the list.")
