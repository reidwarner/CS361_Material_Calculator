import tkinter as tk
from tkinter import ttk, messagebox


class PlanMaterialForm(tk.Frame):
    def __init__(self, parent, controller=None, db=None, selected=None):
        super().__init__(
            parent,
            borderwidth=2,
            relief="solid",
            bg="white",
            pady=5
        )
        self.controller = controller
        self.db = db
        self.selected = selected
        self.combo_values = None
        self.selected_combo_material = None
        self.selected_combo_material_details = None

        all_materials = self.db.get_all_materials()
        self.combo_values_all = [mat[1] for mat in all_materials]

        label_add = tk.Label(self, bg="white", fg="black", text="Add New")
        label_edit = tk.Label(self, bg="white", fg="black", text="Edit Existing")

        # Add new form widgets
        label_1 = tk.Label(self, bg="white", fg="black", text="Material Name")
        label_2 = tk.Label(self, bg="white", fg="black", text="Qty Planned")
        self.combo_1 = ttk.Combobox(self, width=19, values=self.combo_values_all, state="readonly", height=10)
        self.combo_1.bind("<<ComboboxSelected>>", self.on_material_select)
        self.combo_1.bind("<<ButtonRelease-1>>", lambda e: self.after(100, self.on_material_select(e)))
        self.spin_2 = tk.Spinbox(self, from_=0, to=999, width=19, bg="white", fg="black", highlightthickness=0,
                            highlightbackground="lightgrey")
        submit = tk.Button(self, highlightbackground="white", highlightthickness=0, borderwidth=2,
                           bg="lightgrey", text="Add", command=self.plan_material)
        cancel = tk.Button(self, highlightbackground="white", bg="lightgrey", text="Cancel", command=self.cancel_form)

        self.selected_radio = tk.StringVar(value="add")

        add_widgets = [label_1, label_2, self.combo_1, self.spin_2, submit, cancel]

        # Edit material form widgets
        self.spin_qty_planned = tk.Spinbox(self, from_=0, to=999, width=19, bg="white", fg="black", highlightthickness=0,
                                      highlightbackground="lightgrey")
        label_qty_reserve = tk.Label(self, bg="white", fg="black", text="Reserve Material Qty")
        self.spin_qty_reserve = tk.Spinbox(self, from_=0, to=999, width=19, bg="white", fg="black", highlightthickness=0,
                   highlightbackground="lightgrey")

        make_changes_btn = tk.Button(self, highlightbackground="white", highlightthickness=0, borderwidth=2,
                           bg="lightgrey", text="Make Changes", command=self.plan_material)

        edit_widgets = [self.spin_qty_reserve, self.spin_qty_planned, label_qty_reserve, make_changes_btn]

        def radio_select():

            for wid in edit_widgets:
                wid.grid_forget()

            for wid in add_widgets:
                wid.grid_forget()

            if self.selected_radio.get() == "add":
                self.combo_1.configure(values=self.combo_values_all)
                label_1.grid(row=1, column=0, pady=5, padx=5, sticky="w")
                label_2.grid(row=2, column=0, pady=5, padx=5, sticky="w")
                self.combo_1.grid(row=1, column=1, pady=5, padx=5)
                self.spin_2.grid(row=2, column=1, pady=5, padx=5)
                submit.grid(row=3, column=0, pady=5, padx=5)
                cancel.grid(row=3, column=1, pady=5, padx=5)

            else:
                self.combo_1.configure(values=self.combo_values)
                label_1.grid(row=1, column=0, pady=5, padx=5)
                self.combo_1.grid(row=1, column=1, pady=5, padx=5)
                label_2.grid(row=2, column=0, pady=5, padx=5)
                self.spin_qty_planned.grid(row=2, column=1, pady=5, padx=5)
                label_qty_reserve.grid(row=3, column=0, pady=5, padx=5)
                self.spin_qty_reserve.grid(row=3, column=1, pady=5, padx=5)
                make_changes_btn.grid(row=4, column=0, pady=5, padx=5)
                cancel.grid(row=4, column=1, pady=5, padx=5)

        radio_add = tk.Radiobutton(self, bg="white", fg="black", value="add", variable=self.selected_radio, command=radio_select)
        radio_edit = tk.Radiobutton(self, bg="white", fg="black", value="edit", variable=self.selected_radio, command=radio_select)
        label_add.grid(row=0, column=0, pady=10, padx=5)
        label_edit.grid(row=0, column=2, pady=10, padx=5)
        radio_add.grid(row=0, column=1, pady=10, padx=5, sticky="w")
        radio_edit.grid(row=0, column=3, pady=10, padx=5, sticky="w")

        radio_select()

    def confirm_free(self, qty, mat_name):
        response = messagebox.askyesno(
            message=f"Please Confirm: {str(qty * -1)} units of {mat_name} should be uncommitted from project?\n\nFreed materials may be committed for other uses and may not be able to be rereserved.")
        return response

    def update_page(self, selected=None):
        self.selected = selected[0]
        bom = self.db.get_project_bom(selected[0])
        self.combo_values = [mat[0] for mat in bom]

    def cancel_form(self):
        self.spin_2.delete(0, "end")
        self.spin_qty_planned.delete(0, "end")
        self.spin_qty_reserve.delete(0, "end")
        self.spin_qty_planned.insert(0, "0")
        self.spin_qty_reserve.insert(0, "0")
        self.spin_2.insert(0, "0")
        self.controller.show_page("ViewSelectedProjectPage", selected=[self.selected])

    def on_material_select(self, event):
        combo = event.widget
        material = combo.get()
        bom = self.db.get_project_bom(self.selected)
        mat_proj = (0, 0, 0)
        if bom:
            for mat in bom:
                if mat[0] == material:
                    mat_proj = mat
                    break

        self.selected_combo_material = material
        self.selected_combo_material_details = self.db.get_material_by_name(material)
        self.spin_2.delete(0, "end")
        self.spin_qty_planned.delete(0, "end")
        self.spin_qty_reserve.delete(0, "end")
        self.spin_qty_planned.insert(0, mat_proj[1])
        self.spin_qty_reserve.insert(0, mat_proj[2])
        self.spin_2.insert(0, mat_proj[1])

    def plan_material(self):
        plan_material = self.selected_combo_material
        material_details = self.db.get_material_by_name(plan_material)
        bom = self.db.get_project_bom(self.selected)
        mat_proj = None
        for mat in bom:
            if mat[0] == plan_material:
                mat_proj = mat
                break

        if self.selected_radio.get() == "add":
            qty_planned = self.spin_2.get()

            if self.selected_combo_material and (int(qty_planned) > 0):
                self.db.plan_new_material(self.selected, material_details[0], qty_planned)
                self.controller.show_page("ViewSelectedProjectPage", selected=[self.selected])
            else:
                pass
        else:
            qty_planned = self.spin_qty_planned.get()
            qty_reserved = self.spin_qty_reserve.get()

            delta_qty_planned = int(qty_planned) - mat_proj[1]
            delta_qty_reserved = int(qty_reserved) - mat_proj[2]
            tot_qty_stock = material_details[4] - delta_qty_reserved
            tot_qty_planned = material_details[5] + delta_qty_planned
            tot_qty_reserved = material_details[6] + delta_qty_reserved

            if self.selected_combo_material and int(qty_reserved) <= int(qty_planned):
                if delta_qty_reserved < 0:
                    response = self.confirm_free(delta_qty_reserved, material_details[1])
                    if not response:
                        return
                self.db.edit_planned_material(self.selected, material_details[0], int(qty_planned), int(qty_reserved))
                self.db.edit_material(tot_qty_stock, tot_qty_planned, tot_qty_reserved, material_details[0])
                self.controller.show_page("ViewSelectedProjectPage", selected=[self.selected])
            else:
                return






