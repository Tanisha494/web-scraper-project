
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation

FILE_NAME = "expenses.csv"

HEADERS = ["date", "category", "description", "amount"]


def create_file():
    """Create CSV file if it does not exist."""
    try:
        with open(FILE_NAME, "x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
    except FileExistsError:
        pass


def get_date():
    """Get a valid date from the user."""
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD format.")


def get_amount():
    """Get a valid positive expense amount."""
    while True:
        try:
            amount = Decimal(input("Enter amount: ").strip())

            if not amount.is_finite() or amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except InvalidOperation:
            print("Invalid amount! Please enter a number.")


def add_expense():
    print("\n===== ADD EXPENSE =====")

    date = get_date()

    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    description = input("Enter description: ").strip()
    amount = get_amount()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def read_expenses():
    """Read all expenses from the CSV file."""
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def view_expenses():
    print("\n===== ALL EXPENSES =====")

    try:
        expenses = read_expenses()

        if not expenses:
            print("No expenses found.")
            return

        for expense in expenses:
            print(
                f"{expense['date']} | "
                f"{expense['category']} | "
                f"{expense['description']} | "
                f"Rs. {expense['amount']}"
            )

    except (OSError, csv.Error, KeyError) as error:
        print("Could not read expenses:", error)


def filter_expenses():
    print("\n===== FILTER EXPENSES =====")

    category = input("Enter category to filter: ").strip().lower()

    try:
        expenses = read_expenses()

        filtered = [
            expense for expense in expenses
            if expense["category"].strip().lower() == category
        ]

        if not filtered:
            print("No expenses found in this category.")
            return

        total = Decimal("0")

        for expense in filtered:
            print(
                f"{expense['date']} | "
                f"{expense['description']} | "
                f"Rs. {expense['amount']}"
            )
            total += Decimal(expense["amount"])

        print("Category total: Rs.", total)

    except (OSError, csv.Error, KeyError, InvalidOperation) as error:
        print("Could not filter expenses:", error)


def category_summary():
    print("\n===== CATEGORY SUMMARY =====")

    try:
        expenses = read_expenses()

        if not expenses:
            print("No expenses available.")
            return

        totals = {}

        for expense in expenses:
            category = expense["category"]
            amount = Decimal(expense["amount"])

            totals[category] = totals.get(
                category, Decimal("0")
            ) + amount

        for category, total in sorted(totals.items()):
            print(f"{category}: Rs. {total:.2f}")

        grand_total = sum(totals.values(), Decimal("0"))
        print("--------------------------")
        print(f"Grand Total: Rs. {grand_total:.2f}")

    except (OSError, csv.Error, KeyError, InvalidOperation) as error:
        print("Could not calculate summary:", error)


def main():
    create_file()

    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
