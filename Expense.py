import tkinter as tk

class ExpenditureCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Expenditure Calculator")


        self.expenses = {}

        
        

        self.label_category = tk.Label(master, text="Expense Category:")
        self.label_category.grid(row=0, column=0, padx=10, pady=5)
        self.entry_category = tk.Entry(master)
        self.entry_category.grid(row=0, column=1, padx=10, pady=5)


        self.label_amount = tk.Label(master, text="Expense Amount:")
        self.label_amount.grid(row=1, column=0, padx=10, pady=5)
        self.entry_amount = tk.Entry(master)
        self.entry_amount.grid(row=1, column=1, padx=10, pady=5)


        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

        self.total_button = tk.Button(master, text="View Total Expenses", command=self.view_total_expenses)
        self.total_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
        

        self.exit_button = tk.Button(master, text="Exit..", command=master.quit)
        self.exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")


    def add_expense(self):
        category = self.entry_category.get()
        amount = float(self.entry_amount.get())

        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

        self.entry_category.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

        print("Expense added successfully!")

#Starting the condition 


    def view_total_expenses(self):
        if not self.expenses:
            print("No expenses added yet.")
        else:
            total_expenses = sum(self.expenses.values())
            message = "Total Expenses:\n"
            for category, amount in self.expenses.items():
                message += f"{category}: ${amount:.2f}\n"
            message += f"Total: ${total_expenses:.2f}"
            print(message)


#Starting main function



def main():
    root = tk.Tk()
    app = ExpenditureCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()



