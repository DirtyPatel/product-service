import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3030))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
