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
    exhaust_state:bool = False
    sprinkeler_state:bool = False
    temp_up_limit:int = 3000
    temp_down_limit:int = 2500
    humidity_up_limit:int  = 80
    humidity_down_limit:int = 60
    temp_var_1: str = ""
    temp_var_2: str = ""
    temp_var_3: str = ""
    temp_var_4: str = ""
    temp_var_5: str = ""
    temp_var_6: str = ""
    temp_var_7: str = ""
    temp_var_8: str = ""
    temp_var_9: str = ""
    temp_var_10: str = ""
    override:bool = False
    reset:bool = False
    class Config():
        orm_mode = True