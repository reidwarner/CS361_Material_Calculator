import tkinter as tk
from tkinter import ttk
from model.project_model import post_new_project


class CreateProjectForm(tk.Frame):
    def __init__(self, parent, controller, db=None):
        super().__init__(
            parent,
            borderwidth=2,
            relief="solid",
            bg="white"
        )
        self.controller = controller
        self.db = db

        self.label_1 = tk.Label(self, bg="white", fg="black", text="Project Name")
        self.label_2 = tk.Label(self, bg="white", fg="black", text="Est. Completion Date")
        self.label_3 = tk.Label(self, bg="white", fg="black", text="Owner")

        self.entry_1 = tk.Entry(self, bg="white", fg="black", highlightthickness=0)
        self.entry_2 = tk.Entry(self, bg="white", fg="black", highlightthickness=0)
        self.entry_3 = tk.Entry(self, bg="white", fg="black", highlightthickness=0)

        self.submit = tk.Button(self, highlightbackground="white", text="Create", command=self.add_project)
        self.cancel = tk.Button(self, highlightbackground="white", text="Cancel", command=self.cancel_form)

        self.label_1.grid(row=0, column=0, pady=5, padx=5)
        self.label_2.grid(row=1, column=0, pady=5, padx=5)
        self.label_3.grid(row=2, column=0, pady=5, padx=5)

        self.entry_1.grid(row=0, column=1, pady=5, padx=5)
        self.entry_2.grid(row=1, column=1, pady=5, padx=5)
        self.entry_3.grid(row=2, column=1, pady=5, padx=5)

        self.submit.grid(row=3, column=0, pady=5)
        self.cancel.grid(row=3, column=1, pady=5)

        self.error = tk.Label(self, bg="white", fg="red", text="Please enter all details")

    def add_project(self):
        new_project_name = self.entry_1.get()
        new_comp_date = self.entry_2.get()
        new_owner = self.entry_3.get()

        if new_project_name == '' or new_comp_date == '' or new_owner == '':
            self.error.grid(row=4, column=0, pady=5)
        else:
            self.db.add_new_project(new_project_name, new_comp_date, new_owner)
            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_3.delete(0, tk.END)
            self.error.grid_forget()
            self.controller.show_page("ProjectsPage", update=True)

    def cancel_form(self):
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        self.entry_3.delete(0, tk.END)
        self.error.grid_forget()
        self.controller.show_page("ProjectsPage", update=False)
