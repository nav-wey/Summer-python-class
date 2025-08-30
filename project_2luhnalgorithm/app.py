def verify_card_number(card_number: str) -> bool:
    """
    Verify a credit/debit card number using the Luhn algorithm.

    The Luhn algorithm is a simple checksum formula used to validate
    identification numbers such as credit card numbers.

    Steps:
        1. Reverse the card number.
        2. Double every second digit (from the right).
        3. If doubling produces a number >= 10, sum its digits (or subtract 9).
        4. Sum all digits together.
        5. If the total modulo 10 is 0, the number is valid.

    Args:
        card_number (str): The card number as a string of digits.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """

    # Step 1: Reverse the card number string
    card_number_reversed = card_number[::-1]

    # Step 2: Sum of digits in odd positions (from the right)
    sum_of_odd_digits = 0
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Step 3: Process even-position digits (from the right)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        doubled_digit = int(digit) * 2
        # If doubling gives two digits, sum them (e.g., 12 → 1 + 2 = 3)
        if doubled_digit >= 10:
            doubled_digit = (doubled_digit // 10) + (doubled_digit % 10)
        sum_of_even_digits += doubled_digit

    # Step 4: Combine both sums
    total = sum_of_odd_digits + sum_of_even_digits

    # Step 5: Valid if divisible by 10
    return total % 10 == 0


def main():
    """
    Example program to validate a card number.

    Cleans the card number by removing spaces and dashes,
    then checks if it is valid using the Luhn algorithm.
    """

    # Example card number (contains dashes)
    card_number = '4111-1111-4555-1141'

    # Remove spaces and dashes before validation
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Validate and display result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Run the program
if __name__ == "__main__":
    main()
