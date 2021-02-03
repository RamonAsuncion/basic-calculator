# Fix wrong input for operation return
# Accept fractions written as 1/2
# Return string on how to read it?
# numerator1, denominator1 = map(float, first_number.split('/'))        - Fraction


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
            result_value = 'Undefined'
            print(result_value)
            recalculate()
            exit()
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
        return float(input('Enter first number: '))
    except ValueError:
        # If not a integer will recall the function
        print("Wrong input, please re-enter.")
        get_first_number()


def get_operation():
    try:
        # Gets the operation
        return input('Enter the operation: +,-,*, or /: ')
    except ValueError:
        print("Wrong input")
        # Calls the function again if wrong input
        get_operation()


def get_second_number():
    try:
        # gets the second number
        return float(input('Enter second number: '))
    except ValueError:
        # If not a integer will recall the function
        print("Wrong input, please re-enter.")
        get_second_number()


# Once the result is printed in terminal ask user if wants to continue
def recalculate():
    choice = input('Would you like to continue? (Y for Yes / N for No): ')
    if choice.lower() == 'n':
        exit()
    elif choice.lower() == 'y':
        main()
        exit()
    else:
        recalculate()


def main():
    num1 = get_first_number()
    operation = get_operation()
    num2 = get_second_number()
    result_value = calculator(num1, operation, num2)
    format_value_result_calculation(result_value)
    recalculate()


if __name__ == "__main__":
    main()
