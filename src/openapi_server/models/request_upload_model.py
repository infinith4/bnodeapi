from pydantic import BaseModel

class RequestUploadModel(BaseModel):
    upload_file: bytes
