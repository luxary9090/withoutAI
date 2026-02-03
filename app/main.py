from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional
from fastapi_health import health
import json
app = FastAPI()

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'bd.json')

def json_to_dict_list(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)




@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list

@app.get("/")
def home_page():
    return {"message": "Привет, мир!"}


@app.get("/students/{course}")
def get_all_students_course(course: int):
    students = json_to_dict_list(path_to_json)
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list
