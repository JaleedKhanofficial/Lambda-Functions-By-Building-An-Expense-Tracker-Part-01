# Step 24
# Next, you are going to implement the same logic within the total_expenses function.

# For now, delete both the test function and the print() call.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass
    
        # step 24 // delete both the function print and lambda

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial