'''( 1 ) Exercise 4 - Primitive Quiz - ADVANCED'''
# Princess Jamila Dinglasan

'''( 2 ) Using the "Input" Function'''
# Prints a question and waits for the user's input
ques = input("What is the capital of France? ").lower()
'''( 3 ) "If" Statement {Equal to}'''
# Using the If statement + "==" to state if the input is accurate
# Added elif statements to respond if the input is different / wrong
if ques == "paris":
    print(f"Correct, {ques.capitalize()} is the capital of France!")
else:
    print(f"Wrong, the capital of France is Paris, not {ques.capitalize()}. ")