from fastapi import APIRouter

from .api_v1.users import router


api_router = APIRouter()
api_router.include_router(
    router=router,
)
