import tkinter as tk
from tkinter import ttk, messagebox
from models.transaction import Transaction
from utils.file_handler import FileHandler
from utils.stats import Statistics

FILENAME = "transactions.json"

def add_transaction_gui(amount, category, description): #adds a transaction through the GUI.
    transactions = FileHandler.load_from_file(FILENAME)
    new_transaction = Transaction(amount, category, description).to_dict()
    transactions.append(new_transaction)
    FileHandler.save_to_file(FILENAME, transactions)
    messagebox.showinfo("Success", "Transaction successfully added!")

def show_transactions_gui():#display transactions gui
    transactions = FileHandler.load_from_file(FILENAME)
    if not transactions:
        messagebox.showinfo("Information", "No transactions to display.")
        return

    transactions_window = tk.Toplevel()
    transactions_window.title("Transaction List")
    transactions_window.geometry("600x400")

    tree = ttk.Treeview(transactions_window, columns=("Date", "Category", "Amount", "Description"), show="headings")
    tree.heading("Date", text="Date")
    tree.heading("Category", text="Category")
    tree.heading("Amount", text="Amount")
    tree.heading("Description", text="Description")

    for t in transactions:
        tree.insert("", tk.END, values=(t["date"], t["category"], t["amount"], t["description"]))

    tree.pack(fill=tk.BOTH, expand=True)

def start_gui(): #main function to start gui
    root = tk.Tk()
    root.title("Personal Finance Manager")
    root.geometry("400x300")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12))

    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(main_frame, text="Amount:").grid(row=0, column=0, sticky=tk.W, pady=5)
    ttk.Label(main_frame, text="Category:").grid(row=1, column=0, sticky=tk.W, pady=5)
    ttk.Label(main_frame, text="Description:").grid(row=2, column=0, sticky=tk.W, pady=5)

    amount_entry = ttk.Entry(main_frame)
    category_entry = ttk.Entry(main_frame)
    description_entry = ttk.Entry(main_frame)

    amount_entry.grid(row=0, column=1, padx=10, pady=5)
    category_entry.grid(row=1, column=1, padx=10, pady=5)
    description_entry.grid(row=2, column=1, padx=10, pady=5)

    def on_add_transaction():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get().strip()
            description = description_entry.get().strip()

            if not category:
                raise ValueError("Category cannot be empty.")
            
            add_transaction_gui(amount, category, description)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    ttk.Button(main_frame, text="Add Transaction", command=on_add_transaction).grid(row=3, column=0, columnspan=2, pady=10)
    ttk.Button(main_frame, text="Show Transactions", command=show_transactions_gui).grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()
