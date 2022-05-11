from pydantic import BaseModel

class device_type(BaseModel):
    id : str
    os : str

class time_type(BaseModel):
    a: int
    m: int

class file_type(BaseModel):
    file_hash: str
    file_path: str
    time: time_type

class last_acces_type(BaseModel):
    hash: str
    path: str
    pid: int


class Event(BaseModel):
    device: device_type
    file: file_type
    last_access: last_acces_type

