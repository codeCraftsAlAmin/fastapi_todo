from fastapi import FastAPI, Depends, HTTPException, status, Path
from typing import Annotated
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import model, schemas
from model import Todos


app = FastAPI()

model.Base.metadata.create_all(bind=engine)

# generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDp = Annotated[Session, Depends(get_db)]

# base route
@app.get("/todos/", status_code=(status.HTTP_200_OK))
async def get_todos(db: SessionDp):
    return db.query(Todos).all()

# get item by id
@app.get("/todos/{todo_id}", status_code=(status.HTTP_200_OK))
async def get_todo_by_id(db: SessionDp, todo_id: int = Path(gt=0)):
    searched_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if searched_todo is None: 
        raise HTTPException(status_code=404, detail="Data not found")
    return searched_todo

# create route
@app.post("/create_todo/", status_code=(status.HTTP_201_CREATED))
async def create_todo(db: SessionDp, todo_request: schemas.TodoCreate):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

# update route
@app.put("/update_todo/{todo_id}", status_code=(status.HTTP_204_NO_CONTENT))
async def update_todo(db: SessionDp, todo_request: schemas.TodoCreate ,todo_id: int = Path(gt=0)):
    updated_todo = db.query(Todos).filter(Todos.id == todo_id).first()

    if updated_todo is None: 
        raise HTTPException(status_code=404, detail="Data not found")
    
    # updated_todo.title = todo_request.title
    # updated_todo.description = todo_request.description
    # updated_todo.priority = todo_request.priority
    # updated_todo.complete = todo_request.complete

    for key, value in todo_request.model_dump().items():
        setattr(updated_todo, key, value)

    db.add(updated_todo)
    db.commit()


# delete route
@app.delete("/delete_todo/{todo_id}", status_code=(status.HTTP_204_NO_CONTENT))
async def delete_todo(db: SessionDp, todo_id: int = Path(gt = 0)):
    raw_delete = db.query(Todos).filter(Todos.id == todo_id).delete()

    if raw_delete == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    db.commit()
    return 