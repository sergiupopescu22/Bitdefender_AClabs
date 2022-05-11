from pydantic import BaseModel

class file_verdict(BaseModel):
    hash: str
    risk_level: int

class process_verdict(BaseModel):
    hash: str
    risk_level: int

class Verdict(BaseModel):
    file: file_verdict
    process: process_verdict