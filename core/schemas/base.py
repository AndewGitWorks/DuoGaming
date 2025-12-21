from pydantic import  BaseModel, ConfigDict


class SBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)