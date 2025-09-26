from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "THIS IS GET"}

@app.post("/")
async def write_root():
    return {"message": "THIS NOT GET"}
