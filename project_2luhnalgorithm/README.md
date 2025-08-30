# Card Number Validator (Luhn Algorithm)

This project provides a simple implementation of the **Luhn algorithm**
in Python to validate credit or debit card numbers.

------------------------------------------------------------------------

## 📖 How It Works

The Luhn algorithm is a checksum formula used to validate identification
numbers. Many credit card companies use it to verify card numbers before
processing transactions.

### Steps of the Algorithm:

1.  Reverse the card number.
2.  Double every second digit from the right.
3.  If doubling a digit results in a number greater than or equal to 10,
    sum its digits (e.g., 12 → 1 + 2 = 3).
4.  Add together the sum of odd-positioned digits and the processed
    even-positioned digits.
5.  If the total modulo 10 is equal to 0, the number is considered
    **valid**.

------------------------------------------------------------------------

## 📝 Example

Card Number: `4111-1111-4555-1141`

-   Cleaned: `4111111145551141`
-   After applying the algorithm, the result shows: **VALID!**

------------------------------------------------------------------------

## 🚀 Usage

1.  Clone this repository or copy the script.
2.  Run the Python file:

``` bash
python card_validator.py
```

3.  The program will clean the card number (removing dashes and spaces)
    and validate it.

------------------------------------------------------------------------

## 📂 File Structure

    card_validator.py   # Main Python script with the Luhn algorithm
    README.md           # Project documentation

------------------------------------------------------------------------

## ✨ Features

-   Validates card numbers using the Luhn algorithm.
-   Removes spaces and dashes automatically.
-   Simple and beginner-friendly code.

------------------------------------------------------------------------

## 🔧 Future Improvements

-   Accept user input from the terminal.
-   Validate multiple card numbers in one run.
-   Add unit tests for different cases.

------------------------------------------------------------------------

## 🧑‍💻 Author

Developed as a simple Python project demonstrating the **Luhn
Algorithm** for card validation.
