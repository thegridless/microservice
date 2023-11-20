from fastapi import HTTPException
import yaml

def load_data_from_file(filename: str) -> list[dict]:
    try:
        with open(f"builds/{filename}.yaml", "r") as file:
            loaded_data = yaml.safe_load(file)
            return loaded_data.get(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"{filename} not found")