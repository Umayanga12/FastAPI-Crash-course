from fastapi import FastAPI
from fastapi import Path
from typing import Optional

app = FastAPI()

student = {
    1:{
        "name": "John Doe",
        "age" : 20,
        "class" : "science"
    }
}

#creating routers
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/get-studnet/{student_id}")
def get_student(student_id : int = Path(...,description="Invalid Student ID",gt=0)):
    return student[student_id]

#query perameter
@app.get("/get-by-name")
def get_by_name(name: Optional[str]):
    for student_id in student:
        if student[student_id]["name"] == name:
            return  student[student_id]
    return {
        "Data" : "Not Found",
    }