while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ").strip()
    if topping.lower() == 'quit':
        print("Thank you! Your pizza will be prepared.")
        break
    else:
        print(f"I'll add {topping} to your pizza.")
 
