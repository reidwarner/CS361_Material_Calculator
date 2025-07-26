import tkinter as tk
from tkinter import ttk, messagebox


class AdjustQuantity(tk.Frame):
    def __init__(self, parent, controller=None, db=None, material_id=None, selected_material=None):
        super().__init__(
            parent,
            borderwidth=0,
            relief="solid",
            bg="lightgrey"
        )
        self.controller = controller
        self.db = db
        self.material_id = material_id
        self.selected_material = selected_material

        label_1 = tk.Label(self, bg="lightgrey", fg="black", text="Add Stock")
        self.entry_1 = tk.Spinbox(self, bg="white", highlightthickness=0, fg="black", from_=0, to=99)
        submit = tk.Button(self, highlightbackground="lightgrey", text="Add", command=self.confirm_add)
        cancel = tk.Button(self, highlightbackground="lightgrey", text="Cancel")

        label_1.grid(row=0, column=0, pady=5, padx=5)
        self.entry_1.grid(row=0, column=1, pady=5, padx=5)
        submit.grid(row=0, column=2, pady=5, padx=5)
        cancel.grid(row=0, column=3, pady=5, padx=5)

    def confirm_add(self):
        qty = self.entry_1.get()
        if messagebox.askyesno(message=f"Please Confirm: {qty} units of {self.selected_material[1]} should be added to inventory?"):
            self.db.edit_material(self.selected_material[4] + int(qty), self.selected_material[5], self.selected_material[6], self.selected_material[0])

        self.entry_1.delete(0, "end")
        self.entry_1.insert(0, "0")
        self.controller.show_page("ViewSelectedMaterialPage", selected=self.material_id)

    def update_form(self, mat_id, selected_material):
        self.material_id = mat_id
        self.selected_material = selected_material
