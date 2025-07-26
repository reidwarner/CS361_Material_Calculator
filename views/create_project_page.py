import tkinter as tk
from tkinter import ttk
from widgets.create_project_form import CreateProjectForm


class CreateProjectPage(tk.Frame):
    def __init__(self, parent, controller, db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.db = db

        # Page Title
        label = tk.Label(self, bg="lightgrey", fg="black", text="Create New Project", font=("Arial", 28))
        label.pack(pady=20)

        # instructions text
        text = ("Fill out the form below to create a new project.\n"
               "Enter a unique project name.\n"
               "Enter the estimated project completion date.\n"
               "Enter the name of the project owner.\n"
               "Click create to create the new project or cancel to exit the form.")
        instructions = tk.Label(self, bg="lightgrey", fg="black", justify="left", text=text)
        instructions.pack(fill="x", pady=10)

        create_form = CreateProjectForm(self, controller, self.db)
        create_form.pack(pady=10, padx=20, fill="x")
