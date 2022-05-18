import requests
import Send_files.generate_events
from pprint import pprint
import json
import asyncio

def verify_risk(raspuns):

    if raspuns["risk_level"] == -1:
        print("Se va trimite catre serviciul Blackbox")
        with open ("Generated_files/{}".format(raspuns["hash"]),"rb") as file:
            res = requests.post("http://localhost:8001/upload_files/", files = {"file": file.read()})
            print(res.json())
    else:
        print("S-a gasit in CACHE/BAZA DE DATE")


async def testing_event():

    events = []

    with open("events.json",'r') as file:
        data = file.read()
        events = json.loads(data)

    for event in events:
        res = requests.post("http://localhost:8000/send_event", json=event)
        verdict = res.json()

        print()
        pprint(verdict["file"])

        verify_risk(verdict["file"])

        print("------------------------")

if __name__ == "__main__":
    asyncio.run(testing_event())
