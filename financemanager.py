
"""
Created on Thu Jun 24 12:44:36 2021

@author: Yousif Alyousif
"""

import tkinter as tk
import sqlite3
from tkinter import ttk


#con = sqlite3.connect('FinanceManager.db')
#cur = con.cursor()
#cur.execute("""CREATE TABLE finances (
#          item blob,
#          expense blob,
#          qty blob,
#          sign blob,
#          date blob
#          )""")
             
# save function + clear entry boxes
def record():
    con = sqlite3.connect('FinanceManager.db')
    cur = con.cursor()
    cur.execute("INSERT INTO finances VALUES (:item_v, :expense_v, :qty_v, :sign_v, :date_v)",
              {
                  'item_v': item_entry.get(),
                  'expense_v': expense_entry.get(),
                  'qty_v': qty_entry.get(),
                  'sign_v': sign_entry.get(),
                  'date_v': date_entry.get()
              })
    
    con.commit()
    con.close()
    item_entry.delete(0, 50)
    expense_entry.delete(0, 50)
    qty_entry.delete(0, 50)
    sign_entry.delete(0, 50)
    date_entry.delete(0, 50)
    
# display function
def display():
    con = sqlite3.connect('FinanceManager.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM finances")
    financial_records = cur.fetchall()
    for record in financial_records:
        print(record)
        tree.insert("", tk.END, values=record)
    con.commit()
    con.close() 

# remove function
def remove():
    con = sqlite3.connect('FinanceManager.db')
    cur = con.cursor()
    cur.execute("DELETE from finances WHERE oid = " + delete_entry.get())
    delete_entry.delete(0, 50)
    con.commit()
    con.close()
    
# gui
window = tk.Tk()
item_entry = tk.Entry(window, width=20)
item_entry.grid(row=1, column=0, padx=20)
expense_entry = tk.Entry(window, width = 20)
expense_entry.grid(row=1, column=1, padx=20)
qty_entry = tk.Entry(window, width=10)
qty_entry.grid(row=1, column=2, padx=20)
sign_entry = tk.Entry(window, width=10)
sign_entry.grid(row=1, column=3, padx=20)
date_entry = tk.Entry(window, width=10)
date_entry.grid(row=1, column=4, padx=20)
delete_entry = tk.Entry(window, width=10)
delete_entry.grid(row=1, column=6, padx=20)
item_label = tk.Label(window, text='Item')
item_label.grid(row=0, column=0, padx=20)
expense_label = tk.Label(window, text='Expense')
expense_label.grid(row=0, column=1, padx=20)
qty_label = tk.Label(window, text='Qty')
qty_label.grid(row=0, column=2, padx=20)
sign_label = tk.Label(window, text='Signed By')
sign_label.grid(row=0, column=3, padx=20)
date_label = tk.Label(window, text='Date')
date_label.grid(row=0, column=4, padx=20)
save_button = tk.Button(window, text='Save', command=record)
save_button.grid(row=0, column=5, padx=20)
delete_button = tk.Button(window, text='Remove Record', command=remove)
delete_button.grid(row=0, column=6, padx=20)

tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
tree.grid(columnspan=5)
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Item")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Expense")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Qty")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Signed")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Date")
display_button = tk.Button(window, text='Display Expense Records', command=display)
display_button.grid(row=1, column=5, padx=20)

window.mainloop()