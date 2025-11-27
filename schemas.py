from pydantic import BaseModel, Field

from datetime import datetime

from model import Status

class TodoBase(BaseModel):
    # id: int 
    title: str = Field(max_length=50)
    description: str = Field(max_length=60)
    priority: Status = Field(description="pending, processing or complete")
    complete: bool = False

class TodoCreate(TodoBase):
    pass # same as base

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes" : True # necessarry to read sql alchemy object
    }