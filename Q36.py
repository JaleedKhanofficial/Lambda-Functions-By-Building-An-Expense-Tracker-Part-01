# Step 36
# Provide the other menu options by printing the following three strings in your while loop: '3. Show total expenses', '4. Filter expenses by category', and '5. Exit'. Keep adding the print() calls in order.


def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')                     # step 36
        print('4. Filter expenses by category')                     # step 36
        print('5. Exit')                     # step 36
        

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial