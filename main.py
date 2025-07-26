from app import App
from model.database import Database

if __name__ == "__main__":
    db = Database()
    db.db_tables_setup()
    app = App(db=db)
    app.mainloop()



