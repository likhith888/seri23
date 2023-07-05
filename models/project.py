from pydantic import BaseModel

class Project(BaseModel):
    name:str
    description:str
    owner_id:int
    internal_temp:int
    external_temp:int
    internal_humidity:int
    external_humidity:int
    roof_temp:int
    roof_humidity:int
    exhaust_state:bool
    sprinkeler_state:bool
    class Config():
        orm_mode = True