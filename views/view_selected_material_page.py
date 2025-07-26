import tkinter as tk
from tkinter import ttk
from widgets.adjust_quantity import AdjustQuantity


class ViewSelectedMaterialPage(tk.Frame):
    def __init__(self, parent, controller, selected=[], db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.selected_material = None
        self.material_id = selected
        self.db = db

        # Page Title
        self.label = tk.Label(self, bg="lightgrey", fg="black", text="Material Details", font=("Arial", 28))
        self.label.pack(fill="x", side="top")

        # Material Details Table
        columns = ("UID", "Material Name", "Type", "Low Trigger", "Qty In Stock", "Qty Planned", "Qty Reserved")
        where_used_columns = ("Project ID", "Project Name", "Qty Planned", "Qty Reserved")

        self.tree_details = ttk.Treeview(self, columns=columns, show="headings", height=1)
        self.tree_where_planned = ttk.Treeview(self, columns=where_used_columns, show="headings", height=5)

        # Define headings
        for col in columns:
            self.tree_details.heading(col, text=col)
            self.tree_details.column(col, stretch=True, width=50, anchor="center")

        for col in where_used_columns:
            self.tree_where_planned.heading(col, text=col)
            self.tree_where_planned.column(col, stretch=True, width=50, anchor="center")

        # Insert data
        self.tree_details.pack(expand=True, fill="x", padx=5, pady=5)

        self.adj_qty = AdjustQuantity(self, controller=self.controller, db=self.db, material_id=self.material_id, selected_material=self.selected_material)
        self.adj_qty.pack(expand=True, pady=10, fill="x")

        label_where_used = tk.Label(self, bg="lightgrey", fg="black", text="Where Planned", font=("Arial", 22))
        label_where_used.pack(fill="x", side="top")

        self.tree_where_planned.pack(expand=True, fill="x", padx=5, pady=5)

    def update_page(self, uid):
        self.material_id = uid

        to_del = [x for x in self.tree_details.get_children()]
        for x in to_del:
            self.tree_details.delete(x)

        to_del = [x for x in self.tree_where_planned.get_children()]
        for x in to_del:
            self.tree_where_planned.delete(x)

        material = self.db.get_material_by_id(self.material_id)
        data_where_used = self.db.get_material_where_used(self.material_id)
        self.adj_qty.update_form(self.material_id, material)

        for project in data_where_used:
            project_details = self.db.get_project_by_id(project[1])
            row = (project_details[0], project_details[1], project[3], project[4])
            self.tree_where_planned.insert("", tk.END, values=row)

        self.tree_details.insert("", tk.END, values=material)
        self.label.configure(text=f'{material[1]} Details')



