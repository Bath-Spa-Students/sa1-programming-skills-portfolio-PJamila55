'''( 1 ) Exercise 4 - Primitive Quiz'''
# Princess Jamila Dinglasan

'''( 2 ) Using the "Input" Function'''
ques = input ("What is the capital of France? ")

'''( 3 ) "If" Statement {Equal to}'''
if ques == "Paris":
    print(f"Correct, {ques} is the capital of France!")
elif ques == "paris":
    print(f"Correct, but don't forget to add capitalization for the name of a city (Ex: Paris) instead of {ques}.")
elif ques != "paris" or "Paris":
    print(f"Wrong, the capital of France is Paris, not {ques}. ")
