from fastapi import FastAPI, File, UploadFile
from typing import Optional
from pydantic import BaseModel
import aiohttp
import asyncio
import uvicorn
from enum import Enum

from Send_files.model_event import Event
from Send_files.model_verdict import Verdict, process_verdict, file_verdict

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}


@app.post("/send_event", response_model=Verdict)
async def send_event(event: Event):
    return Verdict(file = file_verdict(hash = event.file.file_hash,risk_level = -1),
                                 process = process_verdict(hash = event.last_access.hash, risk_level = -1))


if __name__ == "__main__":
    uvicorn.run(app)


