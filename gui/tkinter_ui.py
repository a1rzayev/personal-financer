import tkinter as tk
from tkinter import messagebox
from models.transaction import Transaction
from utils.file_handler import FileHandler
from utils.stats import Statistics

FILENAME = "transactions.json"

def add_transaction_gui(amount, category, description): #add transaction in gui
    transactions = FileHandler.load_from_file(FILENAME)
    new_transaction = Transaction(amount, category, description).to_dict()
    transactions.append(new_transaction)
    FileHandler.save_to_file(FILENAME, transactions)
    messagebox.showinfo("Success", "Transaction was added")

def show_transactions_gui(): #show transaction in gui
    transactions = FileHandler.load_from_file(FILENAME)
    if not transactions:
        messagebox.showinfo("Info", "There are no transactions")
        return

    transactions_window = tk.Toplevel()
    transactions_window.title("Transactions")

    for idx, t in enumerate(transactions):
        tk.Label(transactions_window, text=f"{t['date']} | {t['category']} | {t['amount']} | {t['description']}").pack()

def start_gui(): #main func to start gui
    root = tk.Tk()
    root.title("Personal Financer")

    tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(root, text="Description:").grid(row=2, column=0, padx=5, pady=5)

    amount_entry = tk.Entry(root)
    category_entry = tk.Entry(root)
    description_entry = tk.Entry(root)

    amount_entry.grid(row=0, column=1, padx=5, pady=5)
    category_entry.grid(row=1, column=1, padx=5, pady=5)
    description_entry.grid(row=2, column=1, padx=5, pady=5)

    def on_add_transaction():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get().strip()
            description = description_entry.get().strip()

            if not category:
                raise ValueError("Category must not be empty")
            
            add_transaction_gui(amount, category, description)
        except ValueError as e:
            messagebox.showerror("Error", f"Wrong login credentials: {e}")

    tk.Button(root, text="Add transaction", command=on_add_transaction).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Show transaction", command=show_transactions_gui).grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()
