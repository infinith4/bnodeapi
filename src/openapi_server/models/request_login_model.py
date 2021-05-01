from pydantic import BaseModel

class RequestLoginModel(BaseModel):
    mail_address: str
    password: str
