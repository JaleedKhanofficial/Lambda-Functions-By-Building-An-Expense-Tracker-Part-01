# Step 22
# You should see something like <map object at 0xd273a8> printed on the console, which is the string representation of the map object returned by map().

# To obtain a readable output you need to turn the map object into a list. Do it by passing the map() call as the argument to the list() function.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass
    
test = lambda x: x * 2
print(list(map(test, [2, 3, 5, 8])))                # step 22

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial