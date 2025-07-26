import tkinter as tk
from tkinter import ttk


class AlertsPage(tk.Frame):
    def __init__(self, parent, controller, db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.selected_material = None
        self.db = db
        self.data_low = []
        self.data_short = []

        # Shortage Table
        columns = ("Material Name", "Qty In Stock", "Qty Planned", "Qty Reserved")

        self.tree_shortages = ttk.Treeview(self, columns=columns, show="headings", height=5)
        self.tree_low = ttk.Treeview(self, columns=columns, show="headings", height=5)

        # Define headings
        for col in columns:
            self.tree_shortages.heading(col, text=col)
            self.tree_shortages.column(col, stretch=True, width=150, anchor="center")
            self.tree_low.heading(col, text=col)
            self.tree_low.column(col, stretch=True, width=150, anchor="center")



        label_shortage = tk.Label(self, bg="lightgrey", fg="black", text="Inventory Shortages", font=("Arial", 22))
        label_shortage.pack(fill="x", side="top")

        self.tree_shortages.bind("<<TreeviewSelect>>", self.material_select)
        self.tree_shortages.pack(expand=True, fill="x", padx=5, pady=5)

        label_low = tk.Label(self, bg="lightgrey", fg="black", text="Low Inventory", font=("Arial", 22))
        label_low.pack(fill="x", side="top")

        self.tree_low.bind("<<TreeviewSelect>>", self.material_select)
        self.tree_low.pack(expand=True, fill="x", padx=5, pady=5)

    def material_select(self, event):
        self.selected_material = self.tree_shortages.selection()

        # Add a scrollbar
        # scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
        # tree.configure(yscrollcommand=scrollbar.set)
        # scrollbar.pack(side="right", fill="y")

    def update_page(self):
        to_del = [x for x in self.tree_low.get_children()]
        for x in to_del:
            self.tree_low.delete(x)

        to_del = [x for x in self.tree_shortages.get_children()]
        for x in to_del:
            self.tree_shortages.delete(x)

        inventory = self.db.get_all_materials()
        self.data_short = []
        self.data_low = []
        for mat in inventory:
            if mat[4] == 0:
                self.data_short.append((mat[1], str(mat[4]), str(mat[5]), str(mat[6])))
            elif mat[4] <= mat[3]:
                self.data_low.append((mat[1], str(mat[4]), str(mat[5]), str(mat[6])))

        # Insert data
        for row in self.data_short:
            self.tree_shortages.insert("", tk.END, values=row)

        # Insert data
        for row in self.data_low:
            self.tree_low.insert("", tk.END, values=row)



