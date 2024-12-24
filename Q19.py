# Step 19
# Lambda functions are brief, anonymous functions in Python, ideal for simple, one-time tasks. They are defined by the lambda keyword, and they use the following syntax:

# Example Code
# lambda x: expr
# In the example above, x represents a parameter to be used in the expression expr, and it acts just like any parameter in a traditional function. expr is the expression that gets evaluated and returned when the lambda function is called.

# Create a variable named test and assign it a lambda function that takes an x parameter and returns x * 2.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass
    
test = lambda x:x*2         # step 19 

expenses = []

# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial