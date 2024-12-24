# Step 28
# Next, define a function named filter_expenses_by_category that takes two parameters: expenses and category. Use pass to fill the function body.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):            # step 28
    pass                                                        # step 28

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial