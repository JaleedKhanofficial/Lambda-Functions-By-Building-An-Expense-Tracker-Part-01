# Step 16
# Next, you are going to display the details for each expense.

# Inside the for loop, replace pass with a print() call and pass it the following f-string: f'Amount: {expense}, Category: {expense}'.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense}, Category: {expense}')        # step 16

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial