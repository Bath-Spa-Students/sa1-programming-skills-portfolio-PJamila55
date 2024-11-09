'''( 1 ) Exercise 10 - Is It Even?'''
# Princess Jamila Dinglasan

'''( 2 ) Function to Check Even or Odd'''
def even_or_odd(num):
    if num % 2 == 0:
        return "The number is even." 
    else:
        return "The number is odd."

'''( 3 ) Getting User Input'''
def main():
    user_number = int(input("Enter a number: "))
    
    result = even_or_odd(user_number)
    print(result)

'''( 4 ) Running the Main Function'''
if __name__ == "__main__":
    main()
