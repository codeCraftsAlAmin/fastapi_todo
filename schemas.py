from pydantic import BaseModel, Field

from datetime import datetime


class TodoBase(BaseModel):
    # id: int 
    title: str = Field(max_length=50)
    description: str = Field(max_length=60)
    priority: int = Field(gt=0, lt=6, description="1 to 5 priority level")
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