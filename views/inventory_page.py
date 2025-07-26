import tkinter as tk
from tkinter import ttk


class InventoryPage(tk.Frame):
    def __init__(self, parent, controller, update=False, db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.selected_material = None
        self.update = update
        self.db = db
        self.types = []

        # Page Title
        self.label = tk.Label(self, bg="lightgrey", fg="black", text="Inventory", font=("Arial", 28))
        self.label.pack(fill="x", side="top")

        # button frame
        self.frame_btn = tk.Frame(self, bg="lightgrey")
        self.frame_btn.pack(fill="x")

        # Add New Material Button
        self.new_material_btn = tk.Button(self.frame_btn, bg="white", highlightbackground="lightgrey", text='Add Material',
                                    command=lambda: controller.show_page("AddMaterialPage"))
        self.new_material_btn.pack(padx=5, pady=5, side="left")

        # View Archive Button
        self.view_alerts_btn = tk.Button(self.frame_btn, highlightbackground="lightgrey", text='View Alerts',
                                     command=lambda: controller.show_page("AlertsPage", update=True))
        self.view_alerts_btn.pack(padx=5, pady=5, side="left")

        # View Selected Project Button
        self.view_material_btn = tk.Button(self.frame_btn, highlightbackground="lightgrey", text='View Selected Material',
                                     command=lambda: controller.show_page("ViewSelectedMaterialPage", selected=self.get_selected()))
        self.view_material_btn.pack(padx=5, pady=5, side="left")

        # Need to add Search
        self.search_frame = tk.Frame(self, bg="lightgrey")
        self.search_frame.pack(fill="x")
        self.search_label = tk.Label(self.search_frame, text="Search by Category:", bg="lightgrey", fg="black")
        self.search_label.pack(padx=5, pady=5, side="left")
        self.search_inventory = ttk.Combobox(self.search_frame, width=8)

        self.search_inventory.bind('<<ComboboxSelected>>')
        self.search_inventory.pack(padx=5, pady=5, side="left")
        self.search_check = tk.Checkbutton(self.search_frame, text="Only Show In Stock", bg="lightgrey", fg="black")
        self.search_check.pack(padx=5, pady=5, side="left")
        self.search_btn = tk.Button(self.search_frame, text='Search', highlightbackground="lightgrey",
                               command=lambda: print(self.search_inventory.get()))
        self.search_btn.pack(padx=5, pady=5, side="left")

        self.search_text = ("Improve your search:"
                       "\n-Search by Category from the dropdown and/or"
                       "\n-Toggle by showing available stock")
        self.search_label_info = tk.Label(self, text=self.search_text, justify="left", bg="lightgrey", fg="black")
        self.search_label_info.pack(padx=5, pady=5, anchor="nw")


        # Material Table
        columns = ("UID", "Material Name", "Type", "Qty In Stock", "Qty Planned", "Qty Reserved")

        self.tree_frame = tk.Frame(self, bg="lightgrey")
        self.tree_frame.pack(fill="x")

        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings", height=10)

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=True, width=150, anchor="center")

        # Insert data
        self.update_page()

        self.tree.bind("<<TreeviewSelect>>")

        # Add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        self.tree.pack(expand=True, padx=5, pady=5, fill="x")

    def get_selected(self):
        return self.tree.item(item=self.tree.selection()[0])['values'][0]

    def update_page(self):
        to_del = [x for x in self.tree.get_children()]
        for x in to_del:
            self.tree.delete(x)

        materials = self.db.get_all_materials()
        for material in materials:
            row = (material[0], material[1], material[2], material[4], material[5], material[6])
            self.tree.insert("", tk.END, values=row)

        self.types = self.db.get_all_material_types()
        self.search_inventory['values'] = self.types





