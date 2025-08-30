# 🧾 Expense Tracker (Python)

A simple **command-line Expense Tracker** written in Python.\
This program helps users record their expenses, categorize them, and
view totals.

------------------------------------------------------------------------

## 🚀 Features

-   Add an expense (amount + category)
-   List all recorded expenses
-   Show the total of all expenses
-   Filter expenses by category
-   Exit the program gracefully

------------------------------------------------------------------------

## 🛠 How It Works

1.  The program displays a menu with options.
2.  The user selects an action (add, list, total, filter, exit).
3.  Expenses are stored in memory as a list of dictionaries.

Example data structure:

``` python
[
    {'amount': 50.0, 'category': 'Food'},
    {'amount': 20.0, 'category': 'Transport'}
]
```

------------------------------------------------------------------------

## ▶️ Usage

Run the program with:

``` bash
python expense_tracker.py
```

You will see a menu like this:

    Expense Tracker
    1. Add an expense
    2. List all expenses
    3. Show total expenses
    4. Filter expenses by category
    5. Exit

### Example Flow:

    Enter your choice: 1
    Enter amount: 25
    Enter category: Food

    Enter your choice: 2
    All Expenses:
    Amount: 25.0, Category: Food

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Save expenses to a file (CSV/JSON) for persistence.
-   Search expenses by keyword (e.g., "food" → "fast food").
-   Display expenses in a tabular format with alignment.
-   Add colors for better UI (using `colorama` library).

------------------------------------------------------------------------

## 📜 License

This project is open-source and free to use for learning purposes.
