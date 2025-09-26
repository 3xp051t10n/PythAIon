from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
generator = pipeline("text-generation", model="gpt2")

@app.post("/")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "Hello, world!")
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return {"response": result[0]["generated_text"]}
