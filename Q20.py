# Step 20
# To call a lambda function you can use the usual function syntax with a pair of parentheses after the variable name.

# Call your test lambda function and pass 3 as the argument. Then, print the result.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass
    
test = lambda x: x * 2
print(test(3))                  # step 20

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial