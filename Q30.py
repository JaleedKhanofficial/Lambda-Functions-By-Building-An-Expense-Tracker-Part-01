# Step 30
# The filter() function allows you to select items from an iterable, such as a list, based on the output of a function:

# Example Code
# filter(my_function, my_list)
# filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.

# The result of the example above is an iterator containing the elements of my_list for which my_function returns True.

# Within the filter_expenses_by_category function, call filter() passing the lambda function you wrote in the previous step as the first argument and the expenses list as the second argument.

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    filter((lambda expense: expense['category'] == category),expenses)          #step 30

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial