from pydantic import BaseModel

class RequestLoginMessageDTO(BaseModel):
    email: str
    password: str

class ResponseLoginMessageDTO(BaseModel):
    token: str
    expires_in: str