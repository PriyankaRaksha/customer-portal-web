from fastapi import FastAPI
from app.routes import customer

app = FastAPI()

app.include_router(customer.router)

@app.get("/")
def home():
    return {"message": "Customer Portal API Running"}

@app.get("/health")
def health():
    return {"status":"ok"}