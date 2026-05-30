import datetime

# List to store expenses
expenses = []

def add_expense(amount, category):
    date = datetime.date.today()
    expenses.append({
        "amount": amount,
        "category": category,
        "date": str(date)
    })
    print(" Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Expense List ---")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']}")

def total_expenses():
    total = sum(e['amount'] for e in expenses)
    print(f"\n💰 Total Expenses: ₹{total}")

def filter_by_category(category):
    filtered = [e for e in expenses if e['category'].lower() == category.lower()]
    if not filtered:
        print(f"No expenses found in category: {category}")
        return
    print(f"\n--- Expenses in {category} ---")
    for e in filtered:
        print(f"{e['date']} | ₹{e['amount']}")

# Menu-driven program
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Filter by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food/Travel/Shopping/etc.): ")
        add_expense(amount, category)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        category = input("Enter category to filter: ")
        filter_by_category(category)
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")