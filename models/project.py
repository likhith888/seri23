from pydantic import BaseModel

class Project(BaseModel):
    name:str
    description:str
    owner_id:int
    class Config():
        orm_mode = True