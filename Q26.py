# Step 26
# Now, call map() passing your lambda function as the first argument and the expenses list as the second argument.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    map(lambda expense: expense['amount'], expenses)            # step 26

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial