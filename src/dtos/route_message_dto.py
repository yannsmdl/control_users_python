from datetime import date
from typing import Optional
from pydantic import BaseModel

class RequestRouteCreateMessageDTO(BaseModel):
    name: str
    path: str
    method: str

class RequestRouteUpdateMessageDTO(BaseModel):
    name: Optional[str]
    path: Optional[str]
    method: Optional[str]
