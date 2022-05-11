import requests
import Send_files.generate_events
from pprint import pprint
import json

from Send_files.model_event import Event
from Send_files.model_verdict import Verdict, process_verdict, file_verdict

def verify_risk(raspuns):

    if raspuns["risk_level"] == -1:
        #print(raspuns)
        print("se va trimite catre server")
        with open ("{}".format(raspuns["hash"]),"rb") as file:
            res = requests.post("http://localhost:8001/upload_files/", files = {"file": file.read()})
            print(res.json())



def testing_event():

    events = []

    with open("events.json",'r') as file:
        data = file.read()
        events = json.loads(data)

    for event in events:
        #pprint(event)
        res = requests.post("http://localhost:8000/send_event", json=event)
        verdict = res.json()
        print()
        pprint(verdict)
        #print()
        #print(verdict["file"])
        verify_risk(verdict["file"])
        print("------------------------\n")

if __name__ == "__main__":
    testing_event()