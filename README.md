# Expense Tracker

## Overview
The **Expense Tracker** is a Python-based program designed to help users manage and track their expenses. It provides functionality to add expenses, view a list of all expenses, and calculate the total expenditure. This tool is simple and user-friendly, suitable for personal financial management.

## Features
1. **Add Expense**: Users can add an expense by specifying a category and an amount.
2. **View Expenses**: Displays a list of all recorded expenses along with their categories and amounts.
3. **Calculate Total Expenses**: Computes and displays the total amount spent across all categories.
4. **Interactive Menu**: A command-line interface allows users to interact with the program easily.

## Class Description
### `class ExpenseTracker`
This class is the core of the Expense Tracker program. It manages all the expense-related functionalities.

### Methods
#### `__init__(self)`
- Initializes an empty list `self.expenses` to store expense data.

#### `add_expense(self, category, amount)`
- Adds an expense to the tracker.
- **Parameters**:
  - `category` (str): The category of the expense.
  - `amount` (float): The amount of the expense.
- Appends a dictionary containing the category and amount to `self.expenses`.

#### `view_expenses(self)`
- Displays all the recorded expenses with their categories and amounts in a readable format.

#### `total_expenses(self)`
- Calculates and prints the total sum of all expenses in `self.expenses`.

## Usage
### Running the Program
1. Run the script in a Python environment by executing:
   ```bash
   python expense_tracker.py
   ```
2. A menu will appear with the following options:
   - Add Expense
   - View Expenses
   - Total Expenses
   - Quit

### Example Interaction
```
Expense Tracker Menu:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Quit

Enter your choice: 1
Enter the expense category: Food
Enter the expense amount: 20.5
Expense added successfully!

Expense Tracker Menu:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Quit

Enter your choice: 2
Category: Food, Amount: $20.5

Expense Tracker Menu:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Quit

Enter your choice: 3
Total Expenses: $20.5
```

### Exiting
- Select option `4` (Quit) to exit the program.

## Requirements
- Python 3.6 or later

## Notes
- Ensure that the expense amount entered is a valid number.
- The program currently supports only basic functionality without data persistence. All data will be lost upon exiting.

## Future Enhancements
- Add functionality to save and load expenses from a file.
- Implement data validation for user inputs.
- Enhance the user interface with a graphical interface or web application support.

## License
This project is open-source and available under the MIT License.

