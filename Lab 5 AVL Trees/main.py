"""
main.py
This file imports avl_transactions.py and executes AVL tree functions.
It allows the user to repeatedly search for transaction details by Transaction ID.
"""

from avl_transactions import AVLTree

# Create AVL tree instance
avl = AVLTree()
root = None

# Adding transactions
transactions = [
    (1001, 500, "2025-02-01"),
    (1002, -200, "2025-02-05"),
    (1003, 1000, "2025-02-10"),
    (1004, -50, "2025-02-12"),
    (1005, 300, "2025-02-15"),
    (1006, -100, "2025-02-18")
]

for txn in transactions:
    root = avl.insert(root, *txn)

# Display all transactions
print("\nAll Transactions (Sorted by ID):")
avl.inorder(root)

# Get Total Balance
total_balance = avl.get_total_balance(root)
print(f"\nTotal Balance: ${total_balance}")

# Search Transactions in Date Range
start_date = "2025-02-05"
end_date = "2025-02-15"
transactions_in_range = avl.search_by_date_range(root, start_date, end_date)

print(f"\nTransactions from {start_date} to {end_date}:")
for txn in transactions_in_range:
    print(f"Transaction ID: {txn[0]}, Amount: {txn[1]}, Date: {txn[2]}")

# Ask User for Transaction ID in a Loop
while True:
    try:
        user_txn_id = int(input("\nEnter a Transaction ID to search (Enter 0 to exit): "))

        if user_txn_id == 0:
            print("Exiting transaction search. Have a nice day!")
            break

        txn = avl.search(root, user_txn_id)

        if txn:
            print(f"\nTransaction Found:\nTransaction ID: {txn.txn_id}\nAmount: {txn.amount}\nDate: {txn.date}")
        else:
            print("\nTransaction ID not found. Try again.")

    except ValueError:
        print("\nInvalid input! Please enter a valid Transaction ID.")
