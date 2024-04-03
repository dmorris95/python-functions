#Task 1

def addition(num1, num2):
    return(num1 + num2)

def subtraction(num1, num2):
    return(num1 - num2)

def multiplication(num1, num2):
    return(num1 * num2)

def division(num1, num2):
    return(num1 / num2)


#Task 2

user_num1 = float(input("Enter the first number for the operation: "))
user_num2 = float(input("Enter the second number for the operation: "))
user_operation = input("What operation (add, subtract, multiply, divide) would you like to perform between the two numbers? ")


#Task 3

if user_operation == "add" and isinstance(user_num1, float) and isinstance(user_num2, float):
    result = addition(user_num1, user_num2)
    print(f"The result is {result}")
elif user_operation == "subtract" and isinstance(user_num1, float) and isinstance(user_num2, float):
    result = subtraction(user_num1, user_num2)
    print(f"The result is {result}")
elif user_operation == "multiply" and isinstance(user_num1, float) and isinstance(user_num2, float):
    result = multiplication(user_num1, user_num2)
    if result > 1000000000:
        print("The result is outside the bounds of the calculator")
    else:
        print(f"The result is {result}")
elif user_operation == "divide" and isinstance(user_num1, float) and isinstance(user_num2, float):
    if user_num2 == 0:
        print("Nice try, but you can't divide by zero.")
    else:
        result = division(user_num1, user_num2)
        print(f"The result is {result}")
else:
    print("You entered something incorrectly.")



