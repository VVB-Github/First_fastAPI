from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str
    
    class Config:
        Schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }
        
class TodoItem(BaseModel):
    item: str
    
    class Config:
        schema_extra = {
            "example": {
                "item": "Read next charter of the book"
            }
        }
        
class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }