import tkinter as tk
from model.inventory_model import post_new_material


class AddMaterialForm(tk.Frame):
    def __init__(self, parent, controller, db=None):
        super().__init__(
            parent,
            borderwidth=2,
            relief="solid",
            bg="white",
            pady=5
        )
        self.controller = controller
        self.db = db

        self.label_1 = tk.Label(self, bg="white", fg="black", text="Material Name")
        self.label_2 = tk.Label(self, bg="white", fg="black", text="Type")
        self.label_3 = tk.Label(self, bg="white", fg="black", text="Low Inventory Qty")

        self.entry_1 = tk.Entry(self, bg="white", fg="black", highlightthickness=0)
        self.entry_2 = tk.Entry(self, bg="white", fg="black", highlightthickness=0)
        self.entry_3 = tk.Entry(self, bg="white", fg="black", highlightthickness=0)

        self.submit = tk.Button(self, highlightbackground="white", highlightthickness=0, borderwidth=2, bg="lightgrey", text="Add", command=self.add_material)
        self.cancel = tk.Button(self, highlightbackground="white", bg="lightgrey", text="Cancel", command=self.cancel_form)

        self.label_1.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.label_2.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.label_3.grid(row=2, column=0, pady=5, padx=5, sticky="w")

        self.entry_1.grid(row=0, column=1, pady=5, padx=5)
        self.entry_2.grid(row=1, column=1, pady=5, padx=5)
        self.entry_3.grid(row=2, column=1, pady=5, padx=5)

        self.submit.grid(row=3, column=0, pady=5, padx=5)
        self.cancel.grid(row=3, column=1, pady=5, padx=5)

        self.error = tk.Label(self, bg="white", fg="red", text="Please enter all fields.")

    def add_material(self):
        new_material_name = self.entry_1.get()
        new_material_type = self.entry_2.get()
        new_qty_trigger = self.entry_3.get()

        if new_material_name == '' or new_material_type == '' or new_qty_trigger == '':
            self.error.grid(row=4, column=0, pady=5)
        else:
            self.db.add_new_material(new_material_name, new_material_type, new_qty_trigger)
            self.entry_1.delete(0, tk.END)
            self.entry_2.delete(0, tk.END)
            self.entry_3.delete(0, tk.END)
            self.error.grid_forget()
            self.controller.show_page("InventoryPage", update=True)

    def cancel_form(self):
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        self.entry_3.delete(0, tk.END)
        self.error.grid_forget()
        self.controller.show_page("InventoryPage", update=False)