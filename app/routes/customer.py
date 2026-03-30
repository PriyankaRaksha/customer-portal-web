from fastapi import APIRouter

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