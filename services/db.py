"""emulating db using provided files"""
from utils.loader import load_data_from_file

builds_data: dict = load_data_from_file("builds")
tasks_data: dict = load_data_from_file("tasks")
