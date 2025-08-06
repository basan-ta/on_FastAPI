from fastapi import FastAPI, HTTPException
import uvicorn
import datetime 

todos = [
    {
        "todo_id": 1,
        "todo_name": "Setup Virtual Environment",
        "todo_description": "Create and activate a Python virtual environment for your FastAPI project."
    },
    {
        "todo_id": 2,
        "todo_name": "Install FastAPI and Uvicorn",
        "todo_description": "Install FastAPI for building APIs and Uvicorn as the ASGI server."
    },
    {
        "todo_id": 3,
        "todo_name": "Create First API Endpoint",
        "todo_description": "Build a simple GET endpoint returning a welcome message."
    },
    {
        "todo_id": 4,
        "todo_name": "Implement CRUD Operations",
        "todo_description": "Create endpoints for Create, Read, Update, and Delete operations."
    },
    {
        "todo_id": 5,
        "todo_name": "Integrate Pydantic Models",
        "todo_description": "Use Pydantic models to validate request and response data."
    },
    {
        "todo_id": 6,
        "todo_name": "Connect with Database",
        "todo_description": "Setup SQLAlchemy or Tortoise ORM to connect FastAPI with a database."
    },
    {
        "todo_id": 7,
        "todo_name": "Add Authentication",
        "todo_description": "Implement JWT-based authentication for secure API access."
    },
    {
        "todo_id": 8,
        "todo_name": "Handle Middleware & Dependencies",
        "todo_description": "Learn to use dependencies and middlewares for request handling and security."
    },
    {
        "todo_id": 9,
        "todo_name": "Deploy FastAPI App",
        "todo_description": "Deploy your FastAPI application to production using Docker or cloud hosting."
    }
]


app = FastAPI()

@app.get("/")
def index():
    return {"message" : "Welcome to my FastAPI practice app"}

@app.get('/todos/{todo_id:int}')
def get_todo(todo_id:int):
    for todo in todos:
        if todo['todo_id'] == todo_id:
            return todo 
    
    raise HTTPException(status_code=404, detail= "Todo not found")