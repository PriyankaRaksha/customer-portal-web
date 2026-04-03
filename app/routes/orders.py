from fastapi import APIRouter

router = APIRouter()

orders=[]

@router.post("/orders")

def create_order(product:str,amount:int):

    order={
        "product":product,
        "amount":amount
    }

    orders.append(order)