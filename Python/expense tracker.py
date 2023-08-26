import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []
        self.venituri=[]

        self.root.geometry("800x700")

        # self.img=PhotoImage(file="moneyg.png",master=root)
        # self.img_label=tk.Label(root,image=self.img)
        # self.img_label.place(x=0,y=0)

        self.root.configure(bg="orange")

        self.amount_label = tk.Label(root, text="Suma:",fg="white",bg="black")

        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.description_label = tk.Label(root, text="Descriere:",fg="white",bg="black")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.date_label = tk.Label(root, text="Data:",fg="white",bg="black")
        self.date_label.pack()

        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.add_button = tk.Button(root, text="Adauga cheltuieli", command=self.add_expense, bg="black",fg="white",relief="groove",activebackground="brown",highlightcolor="red",highlightbackground="red",font="impact")
        self.add_button.pack()

        self.add_buttorn=tk.Button(root,text="Adauga venituri", command=self.add_ven,bg="black",fg="white",relief="ridge",activebackground="brown",font="impact")
        self.add_buttorn.pack()



        self.tree = ttk.Treeview(root, columns=("Suma", "Descriere", "Data"), show="headings")
        self.tree_title_label = tk.Label(root, text="Cheltuieli", font=("Helvetica", 14, "bold"),fg="red",bg="black")
        self.tree_title_label.pack()
        self.tree.tag_configure("Treeview", foreground="red")
        self.tree.heading("Suma", text="Suma")
        self.tree.heading("Descriere", text="Descriere")
        self.tree.heading("Data", text="Data")
        self.tree.pack()

        self.treee = ttk.Treeview(root, columns=("Suma", "Descriere", "Data"), show="headings")
        self.treee_title_label = tk.Label(root, text="Venituri", font=("Helvetica", 14, "bold"), fg="green",bg="black")
        self.treee_title_label.pack()
        self.treee.heading("Suma", text="Suma")
        self.treee.heading("Descriere", text="Descriere")
        self.treee.heading("Data", text="Data")
        self.treee.pack()


    def add_expense(self):
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()

        if amount and description and date:
            expense = (amount, description, date)
            self.expenses.append(expense)
            self.tree.insert("", "end", values=expense)
        else:
            print("Te rog completeaza toate campurile")

    def add_ven(self):
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()

        if amount and description and date:
            venit = (amount, description, date)
            self.venituri.append(venit)
            self.treee.insert("", "end", values=venit)
        else:
            print("Te rog completeaza toate campurile.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
