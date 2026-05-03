from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Elden Ring  API",
    description="Elden Ring build manager API",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
