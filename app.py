import tkinter as tk
from tkinter import ttk
from views.projects_page import ProjectsPage
from views.inventory_page import InventoryPage
from views.archive_projects_page import ArchiveProjectsPage
from views.create_project_page import CreateProjectPage
from views.view_selected_project_page import ViewSelectedProjectPage
from views.add_material_page import AddMaterialPage
from views.view_alerts_page import AlertsPage
from views.view_selected_material_page import ViewSelectedMaterialPage
from views.plan_materials_page import PlanMaterialsPage
from widgets.nav_bar import NavBar


class App(tk.Tk):
    def __init__(self, db=None):
        super().__init__()
        self.title("Material Planner")
        self.geometry("600x600")
        self.current_page = "ProjectsPage"
        self.db = db
        self.pages = (ProjectsPage,
                      InventoryPage,
                      ArchiveProjectsPage,
                      CreateProjectPage,
                      ViewSelectedProjectPage,
                      ViewSelectedProjectPage,
                      AddMaterialPage,
                      AlertsPage,
                      ViewSelectedMaterialPage,
                      PlanMaterialsPage)

        self.container = tk.Frame(self, bg="white")
        self.container.pack(fill="both", expand=True)

        navbar = NavBar(self.container, controller=self)
        navbar.pack(fill="x", padx=5, pady=10)

        self.page_frame = tk.Frame(self.container, bg="lightgrey")
        self.page_frame.pack(fill="x", expand=True, padx=5, anchor="n")

        # Set style
        style = ttk.Style()
        style.theme_use("default")  # Must use a modifiable theme

        # Customize Treeview colors
        style.configure("Treeview",
                        background="white",  # cell background
                        foreground="black",  # cell text
                        fieldbackground="white",  # background when not focused
                        rowheight=25)

        self.frames = {}
        for F in self.pages:
            page_name = F.__name__
            frame = F(parent=self.page_frame, controller=self, db=self.db)
            self.frames[page_name] = frame

        self.show_page(self.current_page)

    def show_page(self, page_name, selected=None, update=False):
        old_page = self.frames[self.current_page]
        old_page.pack_forget()
        frame = self.frames[page_name]
        if selected:
            frame.update_page(selected)
        if update:
            frame.update_page()
        frame.pack(fill="both", expand=True, side="top")
        self.current_page = page_name


