'''( 1 ) Exercise 4 - Primitive Quiz - ADVANCED'''
# Princess Jamila Dinglasan

'''( 2 ) Using the "Input" Function'''
# Prints a question and waits for the user's input
# .lower() is used to make the input case-insensitive

# 1 Paris
paris = input("What is the capital of France? ").lower()

'''( 3 ) "If" Statement {Equal to}'''
# Using the If statement + "==" to state if the input is accurate
# Added elif statements to respond if the input is different / wrong
# .capitalize() is used to make the capitalization of the first letter for each city correct

if paris == "paris":
    print(f"Correct, {paris.capitalize()} is the capital of France! ")
else:
    print(f"Wrong, the capital of France is Paris, not {paris.capitalize()}.")

'''( 4 ) Repeat for the next 9 questions'''

# 2 Germany
germ = input("What is the capital of Germany? ").lower()
if germ == "berlin":
    print(f"Correct, {germ.capitalize()} is the capital of Germany!")
else:
    print(f"Wrong, the capital of Germany is Berlin, not {germ.capitalize()}.")

# 3 Russia
russ = input("What is the capital of Russia? ").lower()
if russ == "moscow":
    print(f"Correct, {russ.capitalize()} is the capital of Russia!")
else:
    print(f"Wrong, Moscow is the capital of Russia, not {russ.capitalize()}.")

# 4 Spain
spin = input("What is the capital of Spain? ").lower()
if spin == "madrid":
    print(f"Correct, {spin.capitalize()} is the capital of Spain!")
else:
    print(f"Wrong, Madrid is the capital of Spain, not {spin.capitalize()}.")

# 5 Switzerland
swiss = input("What is the Swiss capital? ").lower()
if swiss == "bern":
    print(f"Correct, {swiss.capitalize()} is the capital of Switzerland!")
else:
    print(f"Wrong, Bern is the Swiss capital, not {swiss.capitalize()}.")

# 6 Romania
roma = input("What is the capital of Romania? ").lower()
if roma == "bucharest":
    print(f"Correct, {roma.capitalize()} is the capital of Romania!")
else:
    print(f"Wrong, Bucharest is the capital of Romania, not {roma.capitalize()}.")

# 7 Italy
quaso = input("What is the capital of Italy? ").lower()
if quaso == "rome":
    print(f"Correct, {quaso.capitalize()} is the capital of Italy!")
else:
    print(f"Wrong, Rome is the Italian capital, not {quaso.capitalize()}.")

# 8 Sweden
ikea = input("What is the capital of Sweden? ").lower()
if ikea == "stockholm":
    print(f"Correct, {ikea.capitalize()} is the capital of Sweden!")
else:
    print(f"Wrong, the capital of Sweden is Stockholm, not {ikea.capitalize()}")

# 9 Portugal
port = input("What is the capital of Portugal? ").lower()
if port == "lisbon":
    print(f"Correct, {port.capitalize()} is the capital of Portugal!")
else:
    print(f"Wrong, the capital of Portugal is Lisbon, not {port.capitalize()}.")

# 10 Türkiye
turk = input("What is the capital of Türkiye? ").lower()
if turk == "ankara":
    print(f"Correct, the capital of Türkiye is {turk.capitalize()}!")
elif turk == "istanbul":
    print(f"Though {turk.capitalize()} used to be the Türkiye capital, it was changed to Ankara after 1923.")
else:
    print(f"Wrong, the capital of Türkiye is Ankara, not {turk.capitalize()}.")

# TOTAL QUESTIONS: 10 EUROPEAN COUNTRIES
# END - THANK YOU!