from fastapi import APIRouter

router = APIRouter()

@router.post("/payment")

def make_payment(amount:int):

    return {
        "status":"success",
        "amount":amount
    }