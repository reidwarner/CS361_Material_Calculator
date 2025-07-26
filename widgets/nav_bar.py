import tkinter as tk
from tkinter import ttk


class NavBar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(
            parent,
            borderwidth=2,
            relief="solid",
            bg="lightgrey"
        )

        self.btn_projects = tk.Button(self, highlightbackground="lightgrey", text='Projects', command=lambda: controller.show_page("ProjectsPage", update=True))
        self.btn_projects.grid(row=0, column=0, padx=10, pady=5)

        self.btn_inventory = tk.Button(self, highlightbackground="lightgrey", text='Inventory', command=lambda: controller.show_page("InventoryPage", update=True))
        self.btn_inventory.grid(row=0, column=1, padx=10, pady=5)
