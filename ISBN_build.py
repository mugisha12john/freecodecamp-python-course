def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} characters long.')
        return

    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]
    main_digits_list = [int(digit) for digit in main_digits]

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

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
        isbn = values[0].strip()
        length = int(values[1])
        if length in (10, 13):
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')
    except IndexError:
        print('Index error')
    except ValueError:
        print('ValueError')
    finally:
        print('Enter ISBN and length.')


main()