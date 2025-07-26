import tkinter as tk
from tkinter import ttk
from widgets.plan_material_form import PlanMaterialForm


class PlanMaterialsPage(tk.Frame):
    def __init__(self, parent, controller, db=None, selected=None):
        super().__init__(parent, bg="lightgrey", borderwidth=2, relief="solid")
        self.controller = controller
        self.db = db
        self.selected = selected

        # Page Title
        label = tk.Label(self, bg="lightgrey", fg="black", text="Plan Materials for Bird Mansion", font=("Arial", 28))
        label.pack(pady=20)

        # instructions text
        text = ("Select one of the options below."
                " \nSelect 'Add New' to plan a new material for the project."
                " \nSelect 'Edit Existing' to change the planned material quantity and reserve/unreserve"
                " \na planned material quantity."
                " \nClick Add/Make Changes to save your changes or cancel to exit the form.")
        instructions = tk.Label(self, bg="lightgrey", fg="black", text=text, justify="left")
        instructions.pack(pady=10)

        self.create_form = PlanMaterialForm(self, controller=self.controller, db=self.db, selected=self.selected)
        self.create_form.pack(pady=10, padx=20, fill="x")

    def update_page(self, selected=None):
        self.selected = selected
        self.create_form.update_page(selected=self.selected)
