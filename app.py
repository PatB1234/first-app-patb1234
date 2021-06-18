from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from db import *

class Item(BaseModel):
    item: str
    status: bool = False

todos = []
app = FastAPI()
app.mount("/ui", StaticFiles(directory = "ui"), name = "ui")
@app.get("/todo")
def get_todo_items():
    return get_todo_items_from_db()

@app.post("/todo")
def add_todo_item(item: Item):
    todos.append(item)
    post_item_to_todo(item, False)

@app.get("/db")
def get_db():
    return create_tables()

@app.get("/Clear")
def clear_db():
    return clear_table()
