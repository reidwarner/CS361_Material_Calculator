import sqlite3
from model.project_model import data_projects_json
from model.inventory_model import data_materials_json, data_project_bom

#######################
#       DB Setup      #
#######################

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('material_planner.db')
        self.cursor = self.connection.cursor()

    def db_tables_setup(self):
        # Drop tables if they exist
        self.cursor.execute('DROP TABLE IF EXISTS projects')
        self.cursor.execute('DROP TABLE IF EXISTS materials')
        self.cursor.execute('DROP TABLE IF EXISTS materialsPerProject')

        # Create a projects table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS projects (
                        id INTEGER PRIMARY KEY, 
                        title TEXT, 
                        compDate TEXT, 
                        ownerName TEXT,
                        status TEXT)''')

        # Create a materials table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS materials (
                                id INTEGER PRIMARY KEY, 
                                name TEXT, 
                                type TEXT, 
                                qty_low INTEGER,
                                qty_stock INTEGER,
                                qty_planned INTEGER,
                                qty_reserved INTEGER)''')

        # Create a materialsPerProject table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS materialsPerProject (
                                        id INTEGER PRIMARY KEY, 
                                        proj_id INTEGER, 
                                        mat_id INTEGER, 
                                        qty_planned INTEGER,
                                        qty_reserved INTEGER)''')


        # insert initial project data into table
        for project in data_projects_json['project_id'].values():
            self.cursor.execute('''
                    INSERT INTO projects (title, compDate, ownerName, status)
                    VALUES (?, ?, ?, ?)''',
                    (project['title'], project['compDate'], project['ownerName'], project['status']))

        # insert initial project data into table
        for material in data_materials_json['material_id'].values():
            self.cursor.execute('''
                    INSERT INTO materials (name, type, qty_low, qty_stock, qty_planned, qty_reserved)
                    VALUES (?, ?, ?, ?, ?, ?)''',
                    (material['name'], material['type'], material['qty_low'], material['qty_stock'], material['qty_planned'], material["qty_reserved"]))

        for material in data_project_bom:
            self.cursor.execute('''
                                INSERT INTO materialsPerProject (proj_id, mat_id, qty_planned, qty_reserved)
                                VALUES (?, ?, ?, ?)''',
                                material)

        self.connection.commit()

    def get_all_projects(self):
        self.cursor.execute("SELECT * FROM projects")
        return self.cursor.fetchall()

    def get_project_by_id(self, project_id):
        self.cursor.execute(f"SELECT * FROM projects WHERE id = {project_id}")
        return self.cursor.fetchone()

    def get_all_materials(self):
        self.cursor.execute("SELECT * FROM materials")
        return self.cursor.fetchall()

    def get_material_by_id(self, material_id):
        self.cursor.execute(f"SELECT * FROM materials WHERE id = ?", (material_id,))
        return self.cursor.fetchone()

    def get_material_by_name(self, material_name):
        self.cursor.execute(f"SELECT * FROM materials WHERE name = ?", (material_name,))
        return self.cursor.fetchone()

    def add_new_project(self, title, compDate, ownerName):
        self.cursor.execute('''
                            INSERT INTO projects (title, compDate, ownerName, status)
                            VALUES (?, ?, ?, ?)''',
                            (title, compDate, ownerName, 'open'))
        self.connection.commit()

    def get_material_where_used(self, mat_id):
        self.cursor.execute(f"SELECT * FROM materialsPerProject WHERE mat_id = {mat_id}")
        return self.cursor.fetchall()

    def get_all_material_types(self):
        self.cursor.execute('SELECT DISTINCT type FROM materials')
        return self.cursor.fetchall()

    def get_project_bom(self, proj_id):
        self.cursor.execute(f"SELECT * FROM materialsPerProject WHERE proj_id = {proj_id}")
        materials = self.cursor.fetchall()

        bom = []
        for material in materials:
            mat_details = self.get_material_by_id(material[2])
            if not material[4]:
                qty_rsv = 0
            else:
                qty_rsv = int(material[4])
            bom.append((mat_details[1], material[3], qty_rsv, int(material[3]) - int(qty_rsv)))

        return bom

    def add_new_material(self, name, mat_type, qty_low):
        self.cursor.execute('''
                                    INSERT INTO materials (name, type, qty_low, qty_stock, qty_planned, qty_reserved)
                                    VALUES (?, ?, ?, ?, ?, ?)''',
                            (name, mat_type, qty_low, 0, 0, 0))
        self.connection.commit()

    def plan_new_material(self, proj_id, mat_id, qty_planned=0, qty_reserved=0):
        self.cursor.execute('''
                                    INSERT INTO materialsPerProject (proj_id, mat_id, qty_planned, qty_reserved)
                                    VALUES (?, ?, ?, ?)''',
                            (proj_id, mat_id, qty_planned, qty_reserved))
        self.connection.commit()

    def edit_planned_material(self, proj_id, mat_id, qty_planned, qty_reserved):
        self.cursor.execute('''
                                    UPDATE materialsPerProject 
                                    SET qty_planned = ?,
                                        qty_reserved = ?
                                    WHERE proj_id = ? AND mat_id = ?''',
                            (qty_planned, qty_reserved, proj_id, mat_id))
        self.connection.commit()

    def edit_material(self, qty_stock, qty_planned, qty_reserved, mat_id):
        self.cursor.execute('''
                                    UPDATE materials 
                                    SET qty_stock = ?,
                                        qty_planned = ?,
                                        qty_reserved = ?
                                    WHERE id = ?''',
                            (qty_stock, qty_planned, qty_reserved, mat_id))
        self.connection.commit()


request_data = {
    # True means return only search results that have qty_stock > 0. False mean return all results.
    "available": True,
    # The user can select a material type from the drop-down. If a material is selected, only return results with this material type. "type" will be a string or None.
    "type": "wood",
    # Each row in "data" represents an entry in inventory with the following format (matieral_id, material_name, material_type, qty_low_trigger, qty_stock, qty_planned, qty_reserved)
    "data": [
        (1, 'caster wheels', 'misc', 10, 100, 5, 0),
        (2, '2in PVC Elbow', 'pvc', 10, 100, 5, 0),
        (3, '2x4 Cedar', 'wood', 10, 95, 15, 5)
    ]
}


response = {
        # status "ok" means successful and returned results. status "none" means successful but no results based on filter.
        "status": "ok",
        # results returns the material data that reflects the filter options provided
        "results": [
                (3, '2x4 Cedar', 'wood', 10, 95, 15, 5)
            ]
    }





