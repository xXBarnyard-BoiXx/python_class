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
         result = -1
    return result

    return result


operation = input("What operation would you like?(+, -, *, /)\n")
first_number = input("Whats your first number?\n")
first_number = float(first_number)
second_number = input("Whats your second number?\n")
second_number = float(second_number)
result = calculate(first_number, second_number, operation)

if result == -1:
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