from fastapi import FastAPI
import rotor
import requests
from pydantic import BaseModel

app = FastAPI()

reflector = {
    "from": [],
    "to": []
}

class States(BaseModel):
    reflector: str 
    r1_position: str
    r2_position: str
    r3_position: str

global_states = {
    "reflector": None,
    "r1_position": None,
    "r2_position": None,
    "r3_position": None,
}

# @app.get("/")
# def read(q: str, configuration: str | None = None):
#     return {"q": q, "configuration": str}

# to rotor
@app.post("/send")
def send_key(k: str):
    # rotors call 321
    response = requests.get('http://rotor/forward', data={
        "key": k,
        "state": gloabl_states
    }).json()

    # todo: reflector call
    character = reflect(response["char"])

    # todo: rotors call 321
    response = requests.get('http://rotor/backward', data={
        "key": character,
        "state": gloabl_states
    }).json()

    gloabl_states = response["state"]

def reflect(input_char):
    pass
    # todo: do reflection stuff here

# set states
@app.post("/states")
def set_state(states: States):
    print(states)
    global global_states
    
    global_states = states
    return True

# get states
@app.get("/states")
def states():
    return global_states