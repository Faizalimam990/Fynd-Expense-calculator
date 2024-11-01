import os
import csv
from datetime import datetime
from expense import Expense
from category import Category
from report_generator import ReportGenerator
from colorama import init, Fore, Style
import pyfiglet


init(autoreset=True)


banner_text = pyfiglet.figlet_format("Expense Tracker", font="big")
purple_banner = Fore.MAGENTA + banner_text


os.system('cls' if os.name == 'nt' else 'clear')
print(purple_banner)


print(Fore.GREEN + "Welcome to the Expense Tracker!")
print(Fore.CYAN + "Manage your expenses efficiently.")
print(Fore.YELLOW + "Add, view, and delete expenses with ease.")
print(Fore.RED + "Generate insightful reports.")
print(Style.RESET_ALL)
print(Fore.BLUE + "This is a mid course project for Fynd Academy")


class ExpenseTracker:
    def __init__(self, csv_file='expenses.csv'):
        self.csv_file = csv_file
        self.expenses = []
        self.category_manager = Category()
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append(Expense.from_dict(row))
            print("Expenses loaded successfully.")
        else:
            print("No expense data found, starting fresh.")

    def save_expenses(self):
        directory = os.path.dirname(self.csv_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['amount', 'date', 'category', 'description'])
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense.to_dict())
        print(Fore.GREEN + "Expense Saved Successfully")

    def add_expense(self):
        try:
            amount = float(input("Enter amount: "))
            date_input = input("Enter date (YYYY-MM-DD): ")
            date = datetime.strptime(date_input, "%Y-%m-%d")

            categories = self.category_manager.get_categories()
            for i, cat in enumerate(categories):
                print(f"{i + 1}. {cat}")

            category_input = input("Enter the category number or name: ")
            if category_input.isdigit():
                category_index = int(category_input) - 1
                if 0 <= category_index < len(categories):
                    category = categories[category_index]
                else:
                    print("Invalid category number.")
                    return
            elif category_input in categories:
                category = category_input
            else:
                print("Invalid category name.")
                return

            description = input("Enter description: ")
            if not description:
                print("Description cannot be empty.")
                return

            expense = Expense(amount, date_input, category, description)
            self.expenses.append(expense)
            self.save_expenses()

        except ValueError:
            print("Invalid input. Please try again.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 50)
        for expense in self.expenses:
            print(f"{expense.date.strftime('%Y-%m-%d'):<12} {expense.category:<15} {expense.amount:<10} {expense.description}")

    def delete_expense(self, index):
        try:
            self.expenses.pop(index)
            self.save_expenses()
            print("Expense deleted successfully.")
        except IndexError:
            print("Invalid index. Please try again.")

    def filter_by_category(self):
        category = input(f"Enter category to filter by {self.category_manager.get_categories()}: ")
        filtered_expenses = [expense for expense in self.expenses if expense.category == category]

        if not filtered_expenses:
            print(f"No expenses found for category: {category}")
        else:
            print(f"Filtered expenses for category '{category}':")
            for expense in filtered_expenses:
                print(f"{expense.date.strftime('%Y-%m-%d')}: {expense.amount} - {expense.description}")

    def generate_report(self):
        report_gen = ReportGenerator(self.expenses)
        period = input("Generate report for (daily, weekly, monthly): ").lower()
        if period in ['daily', 'weekly', 'monthly']:
            report_gen.generate_report(period)
        else:
            print("Invalid period.")

    def run(self):
        while True:
            print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Filter by Category\n5. Generate Report\n6. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                index = int(input("Enter the index of the expense to delete: "))
                self.delete_expense(index)
            elif choice == '4':
                self.filter_by_category()
            elif choice == '5':
                self.generate_report()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()