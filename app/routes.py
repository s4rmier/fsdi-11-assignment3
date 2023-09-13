from flask import Flask, request
from app.database import task

app = Flask(__name__)


@app.get("/tasks")
def get_all_tasks():
    task_list = task.scan()
    out = {
        "ok": True,
        "tasks": task_list
    }
    return out


@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204


@app.get("/tasks/<int:pk>")
def get_single_task(pk):
    out = {
        "ok": True,
        "task": task
    }

    return out


@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update(task_data, pk)
    return "", 204


@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete(pk)
    return "", 204
