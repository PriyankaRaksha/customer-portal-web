from fastapi import APIRouter
from app.services.customer_service import add_customer

router = APIRouter()

customers = []

@router.post("/customers")
def create_customer(name:str,email:str):

    customer={
        "name":name,
        "email":email
    }

    customers.append(customer)

    return customer

@router.post("/customers/list")

def create_customer(name:str,email:str):

    return add_customer(name,email)