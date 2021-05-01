from pydantic import BaseModel

class RequestLoginUserModel(BaseModel):
    user_id: str
    password: str
