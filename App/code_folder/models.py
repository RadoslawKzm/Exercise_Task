# built in imports
# pip3 install imports
from pydantic import BaseModel

# user created modules


class InfoResponseModel(BaseModel):
    Receiver: str = "is Cisco the best!"


class PingRequestBody(BaseModel):
    url: str = "http://cisco.com"


class PingResponseModel(BaseModel):
    content: str
