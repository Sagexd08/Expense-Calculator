import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# File to store expenses
expense_file = 'expenses.csv'

# Function to add a new expense
def add_expense(amount, category, date=None):
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    
    # Create a DataFrame for new expense
    new_expense = pd.DataFrame({
        'Amount': [amount],
        'Category': [category],
        'Date': [date]
    })
    
    # Try to read the existing file, otherwise create a new one
    try:
        expenses = pd.read_csv(expense_file)
        expenses = pd.concat([expenses, new_expense], ignore_index=True)
    except FileNotFoundError:
        expenses = new_expense

    # Save the expenses back to the CSV file
    expenses.to_csv(expense_file, index=False)
    print("Expense added successfully!")

# Function to show all expenses
def show_expenses():
    try:
        expenses = pd.read_csv(expense_file)
        print(expenses)
    except FileNotFoundError:
        print("No expenses found. Add your first expense.")

# Function to plot expenses by category
def plot_expenses_by_category():
    try:
        expenses = pd.read_csv(expense_file)
        category_group = expenses.groupby('Category')['Amount'].sum()
        plt.figure(figsize=(6, 6))
        
        # Plot the pie chart
        category_group.plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title('Expenses by Category')
        plt.ylabel('')  # Hide y-label as it's redundant in pie chart
        plt.show()

    except FileNotFoundError:
        print("No expenses to show. Please add some expenses first.")

# Function to plot expenses by date
def plot_expenses_by_date():
    try:
        expenses = pd.read_csv(expense_file)
        expenses['Date'] = pd.to_datetime(expenses['Date'])
        
        # Group by date
        date_group = expenses.groupby('Date')['Amount'].sum()
        
        # Plot the line chart
        date_group.plot(kind='line', marker='o', figsize=(8,5))
        plt.title('Expenses by Date')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("No expenses to show. Please add some expenses first.")

# Main menu for user interaction
def main():
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Plot Expenses by Category")
        print("4. Plot Expenses by Date")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Transport, Rent): ")
            date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ") or None
            add_expense(amount, category, date)

        elif choice == '2':
            show_expenses()

        elif choice == '3':
            plot_expenses_by_category()

        elif choice == '4':
            plot_expenses_by_date()

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, please select again.")

# Run the program
if __name__ == "__main__":
    main()
