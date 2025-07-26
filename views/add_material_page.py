import tkinter as tk
from tkinter import ttk
from widgets.add_material_form import AddMaterialForm


class AddMaterialPage(tk.Frame):
    def __init__(self, parent, controller, db=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.db = db

        # Page Title
        label = tk.Label(self, bg="lightgrey", fg="black", text="Add Material", font=("Arial", 28))
        label.pack(pady=20)

        # instructions text
        text = ("Fill out the form below to create a new material."
                " \nGive the material a unique name that is not yet in use. "
                " \nSelect the high-level type of material. "
                "\nEnter the quantity of the new material that will trigger a low stock alert. "
                "\nHit enter to create the new material or cancel to exit the form.")
        instructions = tk.Label(self, bg="lightgrey", fg="black", text=text, justify="left")
        instructions.pack(pady=10)

        create_form = AddMaterialForm(self, controller, self.db)
        create_form.pack(pady=10, padx=20, fill="x")
