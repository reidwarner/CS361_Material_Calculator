import tkinter as tk
from tkinter import ttk


class ProjectsPage(tk.Frame):
    def __init__(self, parent, controller, update=False, db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.update = update
        self.db = db

        # Page Title
        label = tk.Label(self, bg="lightgrey", fg="black", text="Current Projects", font=("Arial", 28))
        label.pack(fill="x", side="top", pady=5)

        # button frame
        frame_btn = tk.Frame(self, bg="lightgrey")
        frame_btn.pack(fill="x", expand=True)

        # Add New Project Button
        new_project_btn = tk.Button(frame_btn, highlightbackground="lightgrey", text='Create New Project', command=lambda: controller.show_page("CreateProjectPage"))
        new_project_btn.grid(row=0, column=0)

        # View Archive Button
        arch_project_btn = tk.Button(frame_btn, highlightbackground="lightgrey", text='View Archived Project', command=lambda: controller.show_page("ArchiveProjectsPage"))
        arch_project_btn.grid(row=0, column=1)

        # View Selected Project Button
        view_project_btn = tk.Button(frame_btn, highlightbackground="lightgrey", text='View Selected Project',
                                     command=lambda: controller.show_page("ViewSelectedProjectPage",
                                     selected=self.get_selected()))
        view_project_btn.grid(row=0, column=2)

        # Project Table
        columns = ("ID", "Project Name", "Estimated Completion Date", "Owner Name")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, stretch=True, width=150, anchor="center")

        # Insert data
        self.update_page()

        self.tree.bind("<<TreeviewSelect>>",)
        self.tree.pack(fill="x", padx=5, pady=5)

    def get_selected(self):
        return self.tree.item(item=self.tree.selection()[0])['values']

    def update_page(self):
        to_del = [x for x in self.tree.get_children()]
        for x in to_del:
            self.tree.delete(x)

        projects = self.db.get_all_projects()
        for proj in projects:
            if proj[4] == 'open':
                self.tree.insert("", tk.END, values=proj)

