from fastapi import HTTPException
from services.db import tasks_data


def find_task_by_name(name: str) -> dict | None:
    for task in tasks_data:
        if task.get("name") == name:
            return task
    return None


def create_tasks_order(tasks_names: list) -> list:
    task_order = []

    def process_task(task_name) -> None:
        task: dict | None = find_task_by_name(task_name)

        if not task:
            raise HTTPException(status_code=404, detail=f"{task_name} not found")

        for dependency in task.get("dependencies"):
            if dependency not in task_order:
                process_task(dependency)

        task_order.append(task.get("name"))

    for task_name in tasks_names:
        if tasks_names not in task_order:
            process_task(task_name)

    return task_order
