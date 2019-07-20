OUT_OF_BOUNDS = float('-inf')



def calculate(first_number, second_number, operation):
    result = 0
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    else:
         result = OUT_OF_BOUNDS
    return result

    return result


more_input = True
while more_input:
    first_number = input("What is the number\n")
    first_number = float(first_number)
    second_number = input("What is the second number?\n")
    second_number = float(second_number)
    operation = input("What Operation do you want to use?\n")
    operation = operation.strip()

    result = calculate(first_number, second_number, operation)
    if result == OUT_OF_BOUNDS:
        print("Please use a valid operator")
    else:
        print(result)
    
    if input("Another calculation (y/n)?") == "y":
        more_input = True
    else:
        more_input = False

operation = input("What operation would you like?(+, -, *, /)\n")
first_number = input("Whats your first number?\n")
first_number = float(first_number)
second_number = input("Whats your second number?\n")
second_number = float(second_number)
result = calculate(first_number, second_number, operation)

if result == OUT_OF_BOUNDS:
    print("Please use a valid operator")
else: 
    print(result)


# if operation == "+":
#     print(first_number + second_number)
# elif operation == "-":
#     print(first_number - second_number)
# elif operation == "*":
#     print(first_number * second_number)
# elif operation == "/":
#     print(first_number / second_number)
# else: print("Please use numbers")