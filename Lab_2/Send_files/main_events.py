import sys, os
import aioredis

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from fastapi import FastAPI, File, UploadFile
import uvicorn
from Scan_files.test_mongo_db import TestDatabase

from Send_files.model_event import Event
from Send_files.model_verdict import Verdict, process_verdict, file_verdict

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}


@app.post("/send_event", response_model=Verdict)
async def send_event(event: Event):
    r = -1
    print("abc")
    #REDIS--------------------------------------------

    redis = aioredis.from_url("redis://localhost")

    value = await redis.get(event.file.file_hash)
    if value is not None:
        print("S-a gasit deja rezultatul in CACHE")
        r = value.decode("utf-8")

    #MONGODB------------------------------------------
    else:
        db = TestDatabase()
        risk = await db.find_data(some_key=event.file.file_hash)

        #SCAN_FILE_API-----------------------------------
        if risk is not None:
            r = risk['risk_level']
            await redis.set(event.file.file_hash, f"{r}")
            print("S-a gasit deja rezultatul in BAZA DE DATE")

    await redis.close()

    return Verdict(file = file_verdict(hash = event.file.file_hash,risk_level = r),
                                 process = process_verdict(hash = event.last_access.hash, risk_level = r))


if __name__ == "__main__":
    #uvicorn.run(app, host='0.0.0.0', port=8000)
    uvicorn.run(app, port=8000)


