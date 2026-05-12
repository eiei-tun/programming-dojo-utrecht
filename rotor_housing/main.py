from fastapi import FastAPI

app = FastAPI()

gloabl_states = {}

@app.get("/")
def read(q: str, configuration: str | None = None):
    return {"q": q, "configuration": str}

@app.post("/states")
def set_state(states):
    print(states)
    gloabl_states = states

@app.get("/states")
def states():
    return gloabl_states