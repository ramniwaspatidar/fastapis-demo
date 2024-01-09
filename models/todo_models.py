
from pydantic import BaseModel

class ToDoMOdel(BaseModel):
    name :str
    description : str
    complete : bool