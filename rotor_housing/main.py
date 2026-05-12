from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_item(q: str | None = None):
    return {"q": q}