from pydantic import BaseModel


class DataModel(BaseModel):
    phone: str
    address: str

    class Config:
        orm_mode = True


class DataInModel(BaseModel):
    phone: str
    address: str
