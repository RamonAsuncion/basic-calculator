import math


def calculator(num1,  operation, num2):
    result_value = ''
    if operation == '+':
        result_value = num1 + num2
    elif operation == '-':
        result_value = num1 - num2
    elif operation == '*':
        result_value = num1 * num2
    elif operation == '/':
        try:
            result_value = num1 / num2
        # checks if divides by 0
        except ZeroDivisionError:
            # returns "undefined" in terminal divide by 0
            result_value = 'Undefined'
            print(result_value)
            # Calls the recalculate function once printed
            recalculate()
            exit()

    elif operation == "sqrt":
        result_value = math.sqrt(num1)
    else:
        main()
    return result_value


def format_value_result_calculation(result_value):
    # add commas to each 3 digits
    if (result_value >= 1000):
        print('Result: {:,.0f}'.format(result_value))
    # if it is an integer eg. 1.0 returns only whole number
    elif result_value.is_integer():
        print('Result: {:.0f}'.format(result_value))
    # if not an integer then leaves the decimal
    else:
        print('Result: {:.3f}'.format(result_value))


def get_first_number():
    try:
        # Gets the first number
        first_number = float(input('Enter first number: '))
    except ValueError:
        # Checks if the input is correct
        print("Wrong input")
        # Calls the function again if wrong input
        get_first_number()
        exit()
        # returns the user input for first number
    return first_number


def get_operation():
    try:
        # Gets the operation
        operation = input('Enter the operation: +,-,*,/, sqrt: ')
    except ValueError:
        print("Wrong input")
        # Calls the function again if wrong input
        get_operation()
        exit()
        # returns the user input for operation
    return operation


def get_second_number():
    try:
        # gets the second number
        second_number = float(input('Enter second number: '))
    except ValueError:
        print("Wrong input")
        # Calls the function again if wrong input
        get_second_number()
        exit()
        # returns the user input for second number
    return second_number


def recalculate():
    # Prints the code below into terminal
    choice = input('Would you like to continue? (Y for Yes / N for No): ')
    # N or n works and stops the script
    if choice.lower() == 'n':
        exit()
    # Y or y works and stops the script
    elif choice.lower() == 'y':
        # Calls the main function
        main()
    else:
        # Wrong input calls the recalculate function again
        recalculate()


def main():
    operation = get_operation()
    num1 = get_first_number()
    num2 = get_second_number()
    result_value = calculator(num1, operation, num2)
    format_value_result_calculation(result_value)
    recalculate()


if __name__ == "__main__":
    main()
