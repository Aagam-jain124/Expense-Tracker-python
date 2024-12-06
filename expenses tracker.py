class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({'category': category, 'amount': amount})

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Category: {expense['category']}, Amount: ${expense['amount']}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
