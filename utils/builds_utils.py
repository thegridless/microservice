from services.db import builds_data


def find_build_by_name(name: str) -> dict | None:
    for build in builds_data:
        if build.get("name") == name:
            return build
    return None
