import tkinter as tk
from tkinter import ttk
from sample_data.sample_project_data import data_current_projects


class ViewSelectedProjectPage(tk.Frame):
    def __init__(self, parent, controller, selected=[], db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.data = selected
        self.db = db

        # Page Title
        self.label = tk.Label(self, bg="lightgrey", fg="black", text=f"{self.data} Details", font=("Arial", 28))
        self.label.pack(fill="x", side="top")

        columns = ("ID", "Project Name", "Estimated Completion Date", "Owner Name")

        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=1)

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=True, width=150, anchor="center")


        self.tree.pack(expand=True, fill="x", padx=5, pady=10)

        # Project Materials
        label_bom = tk.Label(self, bg="lightgrey", fg="black", text="Materials", font=("Arial", 22))
        label_bom.pack(fill="x", side="top")

        # button frame
        frame_2_btn = tk.Frame(self, bg="lightgrey")
        frame_2_btn.pack(fill="x")

        # Plan Button
        plan_material_btn = tk.Button(frame_2_btn, highlightbackground="lightgrey", text='Plan Material',
                                     command=lambda: controller.show_page("PlanMaterialsPage", selected=self.data))
        plan_material_btn.pack(padx=5, side="left")
        columns_bom = ("Material", "Qty Planned", "Qty Reserved", "Qty Needed")

        self.tree_bom = ttk.Treeview(self, columns=columns_bom, show="headings", height=5)

        # Define headings
        for col in columns_bom:
            self.tree_bom.heading(col, text=col)
            self.tree_bom.column(col, stretch=True, width=100, anchor="center")

        self.tree_bom.pack(expand=True, fill="x", padx=5, pady=5)

    def update_page(self, selected):
        self.data = selected
        to_del = [x for x in self.tree.get_children()]
        for x in to_del:
            self.tree.delete(x)

        to_del = [x for x in self.tree_bom.get_children()]
        for x in to_del:
            self.tree_bom.delete(x)

        project = self.db.get_project_by_id(self.data[0])
        self.tree.insert("", tk.END, values=project)

        bom = self.db.get_project_bom(self.data[0])
        for mat in bom:
            self.tree_bom.insert("", tk.END, values=mat)

        self.label.configure(text=f'{project[1]} Details')




        # Add a scrollbar
        # scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
        # tree.configure(yscrollcommand=scrollbar.set)
        # scrollbar.pack(side="right", fill="y")
