# Step 25
# In the total_expenses function, you'll now integrate a lambda function. Replace pass with a lambda function that has expense as its parameter.

# expense is expected to be a dictionary, and your lambda function should return the value of the 'amount' key in the expense dictionary.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    lambda expense:expense["amount"]            # step 25

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial