import sys

def validate_isbn(isbn, length):
    # Check if length is numeric
    if not isinstance(length, int):
        print('Length must be a number')
        return

    # Check length mismatch
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Check for invalid characters
    if not isbn.isdigit():
        print('Invalid character was found.')
        return

    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]

    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    elif length == 13:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    else:
        print('Length should be 10 or 13.')
        return

    # Compare
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (1 if index % 2 == 0 else 3)
    result = 10 - digits_sum % 10
    return '0' if result == 10 else str(result)


def main():
    try:
        user_input = input('Enter ISBN and length (e.g. 9780306406157,13): ')
        values = user_input.split(',')

        # Must be exactly 2 values
        if len(values) != 2:
            print('Enter comma-separated values.')
            return

        isbn = values[0].strip()

        try:
            length = int(values[1].strip())
        except ValueError:
            print('Length must be a number.')
            return

        if length in (10, 13):
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')

    except Exception as e:
        print(f'Unexpected error: {e}')

    finally:
        print('Enter ISBN and length.')


main()