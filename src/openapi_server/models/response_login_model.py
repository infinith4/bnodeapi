from pydantic import BaseModel

class ResponseLoginModel(BaseModel):
    token: str
