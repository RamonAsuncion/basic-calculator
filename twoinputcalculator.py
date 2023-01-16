from fractions import Fraction
from typing import Union

def calculation_of_two_numbers(number1: float,  operation: str, number2: float) -> Union[float, str]:
    """ Compute the value using the two input values and the operation given by the user.

    :param float number1: first input.
    :param str operation: the math operation.
    :param float number2: second input.
    :return: Union[float, str]: the computed value as a string or float.
    """
    # Addition
    if operation == '+':
        return number1 + number2
    # Subtraction
    elif operation == '-':
        return number1 - number2
    # Multiplication
    elif operation == '*':
        return number1 * number2
    # Power
    elif operation == '**' or operation == '^':
        return number1 ** number2
    # Mod
    elif operation == '%':
        return number1 % number2
    # Floor division
    elif operation == '//':
        return number1 // number2
    # Division
    elif operation == '/':
        if number2 == 0:
            return "Undefined"
        return number1 / number2
    else:
        main()

def format_decimal_numbers(result_value: float) -> None:
    """ Print out the formatted result value from the computation.

    :param float: result_value
    :return: None
    """
    if result_value == 'Undefined':
        print(result_value)
    elif (result_value >= 1_000):
        print('Result: {:,.0f}'.format(result_value))
    elif result_value.is_integer():
        print('Result: {:.0f}'.format(result_value))
    else:
        print('Result: {:.3f}'.format(result_value))

def get_first_number() -> float:
    """Get the first numbre from user input.

    :return: float: the first input.
    """
    return float(Fraction(input('Enter first number: ')))

def get_operation() -> str:
    """Get the operation being used to compute the two values.

    :return: str: the math operation.
    """
    return input('Enter the operation: +,-,*, ^ (**), %, //, or /: ')

def get_second_number() -> float:
    """Get the second number from user input.

    :return: float: the second input.
    """
    return float(Fraction(input('Enter second number: ')))

def recalculate() -> None:
    """Prompt the user if they want to continue calculating more values."""
    choice = input('Would you like to continue? (Y for Yes / N for No): ')
    if choice.lower() == 'n':
        exit()
    elif choice.lower() == 'y':
        main()
    else:
        recalculate()

def main():
    number1 = get_first_number()
    operation = get_operation()
    number2 = get_second_number()
    result_value = calculation_of_two_numbers(number1, operation, number2)
    format_decimal_numbers(result_value)
    recalculate()

if __name__ == '__main__':
    main()
