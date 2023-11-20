
from fastapi import APIRouter

from .tasks_router import router as tasks_router

router = APIRouter()
router.include_router(tasks_router)
