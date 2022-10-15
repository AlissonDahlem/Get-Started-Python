from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
  return {"message": "Hello World!"}

@app.get("/{name}")
async def route_19(name: str):
  return {"word": name}