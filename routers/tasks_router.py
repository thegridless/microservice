from fastapi import APIRouter, HTTPException
from models.BuildModel import BuildModel

from utils.builds_utils import find_build_by_name
from utils.tasks_utils import create_tasks_order

router = APIRouter()


@router.post("/get_tasks")
async def get_tasks(BuildModel: BuildModel) -> list:
    build: dict = find_build_by_name(BuildModel.build)
    if not build:
        raise HTTPException(status_code=404, detail=f"{BuildModel.build} not found")
    tasks: list = build.get("tasks")
    if not tasks:
        raise HTTPException(
            status_code=404, detail=f"Tasks for build {BuildModel.build} not found"
        )
    return create_tasks_order(tasks)
