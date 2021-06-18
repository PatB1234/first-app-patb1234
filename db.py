import sqlite3 as db
from pydantic import BaseModel

DATABASE_URL = 'db/todo.db'

class Item(BaseModel):
    item: str
    status: bool = False

def create_tables():
    database = db.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS TODOS (ITEM TEXT, STATUS INT);")

def post_item_to_todo(item:Item, status: bool):
    if status:
        int_status = 1
    else:
        int_status = 0
    with db.connect(DATABASE_URL) as mdb:
        mdb.execute(
            f"INSERT INTO TODOS VALUEs ('{item.item}', '{int_status}');"
        )
        mdb.commit()
def get_todo_items_from_db():
    with db.connect(DATABASE_URL) as mdb:
        return [
            dict(item = m[0], status = m[1])
            for m in mdb.execute(
                f"SELECT * FROM TODOS;"
            ).fetchall()
        ]
def clear_table():
    with db.connect(DATABASE_URL) as mdb:
        mdb.execute(f"DELETE FROM TODOS;")
        mdb.commit()