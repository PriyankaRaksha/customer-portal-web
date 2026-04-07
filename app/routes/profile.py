from fastapi import APIRouter

router = APIRouter()

@router.get("/profile")

def get_profile():

    profile={
        "name":"customer",
        "membership":"gold"
    }

    return profile