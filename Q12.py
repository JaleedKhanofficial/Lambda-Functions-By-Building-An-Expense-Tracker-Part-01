# Step 12
# A dictionary is another built-in data type in Python. A dictionary is a collection of data in the form of key-value pairs. Dictionaries are defined with curly braces ({}) and they contain key-value pairs separated by commas. Each key is followed by a colon (:) and the value:

# Example Code
# {'amount': 50.0, 'category': 'Food'}
# In the example above, 'amount' and 'category' are keys, and 50.0 and 'Food' are their corresponding values.

# Create a dictionary with a key 'amount' and value of the amount parameter and pass your new dictionary to the .append() call.

def add_expense(expenses, amount, category):
    expenses.append({'amount':amount})                  # step 12
    

expenses = []


# GitHub : jaleedkhanofficial
# linkedin.com/in/jaleedkhanofficial