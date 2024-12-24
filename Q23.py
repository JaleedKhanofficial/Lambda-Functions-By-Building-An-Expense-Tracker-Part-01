# Step 23
# The sum() function returns the sum of the items in the iterable which is passed as its argument. You are going to use sum() together with map() and lambda functions to get the total amount of expenses.

# For now, make a little test and modify your current print() call replacing the list() call with a call to the sum() function passing it the current map() call as the argument.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass
    
test = lambda x: x * 2

print(sum(map(test, [2,3,5,8])))                # step 23

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial