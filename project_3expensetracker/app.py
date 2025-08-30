def add_expense(expenses, amount, category):
    # Add a new expense as a dictionary to the expenses list
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    # Print all expenses in a readable format
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    # Calculate the total amount of all expenses using map + sum
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    # Return expenses filtered by a given category
    # NOTE: filter() returns an iterator, so better to cast to list when using
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    # Main program loop with menu-driven options
    expenses = []  # Store all expenses here
    
    while True:
        # Display the menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            # Add a new expense (amount + category)
            try:
                amount = float(input('Enter amount: '))
            except ValueError:
                print("Invalid input! Amount must be a number.")
                continue
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Show all recorded expenses
            print()
