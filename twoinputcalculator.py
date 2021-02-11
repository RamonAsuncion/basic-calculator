# Fix wrong input for operation return
# Accept fractions written as 1/2 and get the gcd to add
# Return string on how to read it?
# have to fix when it treturns wrong input and recalls the method it still has the type from before
from fractions import Fraction


def calculator(number1,  operation, number2):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '^' or operation == '**':
        return number1 ** number2
    elif operation == '%':
        return number1 % number2
    elif operation == '/':
        try:
            return number1 / number2
        # checks if divides by 0
        except ZeroDivisionError:
            result_value = 'Undefined'
            print(result_value)
            recalculate()
            exit()
    else:
        main()


def format_decimal_numbers(result_value):
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
        return float(input('Enter first number: '))
    except ValueError:
        print('Wrong input, please re-enter.')


def get_operation():
    return input('Enter the operation: +,-,*, ^ (**), %, or /: ')


def get_second_number():
    try:
        return float(input('Enter second number: '))
    except ValueError:
        print('Wrong input, please re-enter.')
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
    number1 = get_first_number()
    operation = get_operation()
    number2 = get_second_number()
    result_value = calculator(number1, operation, number2)
    format_decimal_numbers(result_value)
    recalculate()


if __name__ == '__main__':
    main()
