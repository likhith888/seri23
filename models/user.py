from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    password:str
    project_id:str    
    class Config():
        orm_mode = True
