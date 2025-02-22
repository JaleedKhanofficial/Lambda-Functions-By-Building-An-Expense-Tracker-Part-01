# Step 17
# In Python, an important thing to know is that the same type of quote used to define a string cannot be used inside it. For example, the string 'I'm a string!' is not valid. To use the single quote inside that string you should either:

# Escape the quote by prepending a backlash to it: 'I\'m a string!'
# Or use double quotes to define the string: "I'm a string!" (preferred).
# You can access values in a dictionary through its keys. You need to use bracket notation and include the key between the square brackets:

# Example Code
# my_dict = {'amount': 50.0, 'category': 'Food'}
# my_dict['amount'] # 50.0
# You are currently interpolating the expense dictionary in your f-string. Modify the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')          # step 17

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial