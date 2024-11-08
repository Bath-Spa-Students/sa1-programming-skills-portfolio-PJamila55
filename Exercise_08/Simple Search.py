'''( 1 ) Exercise 8 - Simple Search'''
# Princess Jamila Dinglasan

'''( 2 ) Creating Dictionary'''
people = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_term = input("Who are you looking for? ").lower()

'''( 3 ) If - Else Statement'''
if search_term in [name.lower() for name in people]:
    print(f"{search_term.capitalize()} is in the list!")
    print("\n")
else:
    print(f"{search_term.capitalize()} is not on the list.")
    print("\n")
