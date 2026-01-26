from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional
from fastapi_health import health
import json
app = FastAPI()

script_dir = os.path.dirname(os.path.abspath(__file__))
path_to_json = os.path.join(script_dir, 'bd.json')


def json_to_dict_list(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)




@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)
@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}
@app.get("/students/{course}")
def get_all_students_course(course: int):
    students = json_to_dict_list(path_to_json)
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list
