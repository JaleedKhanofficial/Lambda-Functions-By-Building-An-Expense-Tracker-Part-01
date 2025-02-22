# Step 43
# To list all expenses, you can use an elif clause after an if statement. The elif checks additional conditions and only works following an if statement.

# Create an elif clause to check if the user's choice equals the string '2'. Inside the elif clause, print the string '\nAll Expenses:'.


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
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':                 # step 43
            print('\nAll Expenses: ')               #step 43
        
                

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficia