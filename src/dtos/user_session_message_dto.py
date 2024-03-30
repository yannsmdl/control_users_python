from pydantic import BaseModel

class RequestSessionMessageDTO(BaseModel):
    user_id: int
    token: str
    expires_in: str
