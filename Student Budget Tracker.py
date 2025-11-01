# STUDENT BUDGET TRACKER
# This program helps students track their allowance and expenses.
# It includes input validation to prevent invalid entries like negative amounts.

# FUNCTIONS
def show_menu():
    """Display the main menu options."""
    # Print the menu header and options for user selection
    print("\n=== STUDENT BUDGET TRACKER ===")
    print("1. Add Allowance")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

def get_positive_amount(prompt):
    """Get a positive float amount from user with validation.
    
    This helper function ensures the user enters a valid positive number.
    It loops until a valid input is provided.
    """
    while True:  # Keep asking until valid input is received
        try:
            # Attempt to convert input to float
            amount = float(input(prompt))
            if amount <= 0:  # Check if amount is zero or negative
                print("Amount must be positive. Try again.")
            else:
                return amount  # Return the valid positive amount
        except ValueError:  # Handle non-numeric input
            print("Please enter a valid number.")

def add_allowance(transactions, balance):
    """Add an allowance entry with validation.
    
    Prompts for amount and note, adds to transactions list, and updates balance.
    """
    # Get a valid positive amount using the helper function
    amount = get_positive_amount("Enter allowance amount: ")
    # Get the note and remove extra spaces
    note = input("Enter source (e.g., Parents, Part-time job): ").strip()
    # Add the transaction as a dictionary to the list
    transactions.append({"type": "Allowance", "amount": amount, "note": note})
    # Update the balance by adding the amount
    balance += amount
    # Confirm the addition to the user
    print(f"Allowance of ₱{amount:.2f} added successfully.")
    # Add a visual separator
    print("-" * 40)
    return balance  # Return the updated balance

def add_expense(transactions, balance):
    """Add an expense entry with validation and balance check.
    
    Prompts for amount and note, checks if affordable, then adds to transactions and subtracts from balance.
    """
    # Get a valid positive amount using the helper function
    amount = get_positive_amount("Enter expense amount: ")
    # Check if the expense exceeds current balance
    if amount > balance:
        # Inform user and do not record the expense
        print(f"Expense of ₱{amount:.2f} exceeds current balance of ₱{balance:.2f}. Not recorded.")
        print("-" * 40)
        return balance  # Return unchanged balance
    # Get the note and remove extra spaces
    note = input("Enter expense description (e.g., Lunch, Books): ").strip()
    # Add the transaction as a dictionary to the list
    transactions.append({"type": "Expense", "amount": amount, "note": note})
    # Update the balance by subtracting the amount
    balance -= amount
    # Confirm the addition to the user
    print(f"Expense of ₱{amount:.2f} recorded successfully.")
    print("-" * 40)
    return balance  # Return the updated balance

def view_transactions(transactions):
    """Display all transactions with formatting.
    
    Loops through the transactions list and prints each one with numbering.
    """
    if not transactions:  # Check if the list is empty
        print("No transactions yet.")
        print("-" * 40)
    else:
        # Print header for transaction history
        print("\n--- TRANSACTION HISTORY ---")
        # Loop through transactions with 1-based indexing
        for i, t in enumerate(transactions, start=1):
            # Print each transaction with type, amount, and note
            print(f"{i}. {t['type']}: ₱{t['amount']:.2f} ({t['note']})")
        print("-" * 40)  # Add a visual separator

def view_balance(balance):
    """Display the current balance.
    
    Simply prints the balance with two decimal places.
    """
    print(f"\nCurrent Balance: ₱{balance:.2f}")
    print("-" * 40)  # Add a visual separator

# MAIN PROGRAM
def main():
    """Run the main program loop.
    
    Initializes data structures, shows welcome message, and handles user choices in a loop.
    """
    # Initialize empty list for transactions and starting balance
    transactions = []
    balance = 0.0
    # Welcome message to the user
    print("Welcome to the Student Budget Tracker!")
    
    while True:  # Main loop continues until user chooses to exit
        # Show the menu options
        show_menu()
        # Get user's choice and remove extra spaces
        choice = input("Enter your choice (1-5): ").strip()
        
        # Handle each menu choice
        if choice == "1":
            # Add allowance and update balance
            balance = add_allowance(transactions, balance)
        elif choice == "2":
            # Add expense and update balance
            balance = add_expense(transactions, balance)
        elif choice == "3":
            # Show all transactions
            view_transactions(transactions)
        elif choice == "4":
            # Show current balance
            view_balance(balance)
        elif choice == "5":
            # Exit the program with a goodbye message
            print("Thank you for using the Student Budget Tracker. Goodbye!")
            break  # Exit the loop
        else:
            # Handle invalid menu choices
            print("Invalid choice. Try again.")
            print("-" * 40)

# RUN PROGRAM
# This block runs the main function when the script is executed directly
if __name__ == "__main__":
    main()
