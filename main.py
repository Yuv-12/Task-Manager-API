from fastapi import FastAPI

app = FastAPI(title = "Task Manager APT")

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "design an task manager API using FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn Docker",
        "description": "push the task manager API to docker hub",
        "completed": True
    },
    {
        "id": 3,
        "title": "Learn Kubernetes",
        "description": "deploy the task manager API to kubernetes cluster",
        "completed": False
    }
]

@app.get('/')
def home():
    return {"message": "Welcome to the Task Manager API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get('/tasks')
def get_tasks():
    return tasks