import tkinter as tk
from tkinter import ttk


class ArchiveProjectsPage(tk.Frame):
    def __init__(self, parent, controller, db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.db = db

        # Page Title
        label = tk.Label(self, bg="lightgrey", fg="black", text="Archived Projects", font=("Arial", 28))
        label.pack(fill="x", side="top")

        # view button
        view_project_btn = tk.Button(self, highlightbackground="lightgrey", text='View Selected Project',
                                     command=lambda: controller.show_page("ViewSelectedProjectPage",
                                                                          selected=self.get_selected()))
        view_project_btn.pack(anchor="nw")

        # Project Table
        columns = ("ID", "Project Name", "Completion Date", "Owner Name")

        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=True, width=150, anchor="center")

        # Insert data
        self.update_page()

        self.tree.bind("<<TreeviewSelect>>", )
        self.tree.pack(expand=True, fill="x", padx=5, pady=5)

    def get_selected(self):
        return self.tree.item(item=self.tree.selection()[0])['values']

    def update_page(self):
        to_del = [x for x in self.tree.get_children()]
        for x in to_del:
            self.tree.delete(x)

        projects = self.db.get_all_projects()
        for proj in projects:
            if proj[4] == 'closed':
                self.tree.insert("", tk.END, values=proj)


