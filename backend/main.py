from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Habit(BaseModel):
    id: int
    name: str
    completed: bool = False

habits: List[Habit] = []

@app.get("/habits")
def get_habits():
    return habits

@app.post("/habits")
def add_habit(habit: Habit):
    habits.append(habit)
    return habit

@app.put("/habits/{habit_id}")
def toggle_habit(habit_id: int):
    for habit in habits:
        if habit.id == habit_id:
            habit.completed = not habit.completed
            return habit
    return {"error": "Habit not found"}

@app.delete("/habits/{habit_id}")
def delete_habit(habit_id: int):
    global habits
    habits = [h for h in habits if h.id != habit_id]
    return {"message": "Deleted"}
