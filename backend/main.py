from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()

# ---- CORS (IMPORTANT for frontend on Vercel) ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for demo / portfolio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Data Model ----
class Habit(BaseModel):
    id: int
    name: str
    completed: bool = False

habits: List[Habit] = []

# ---- Routes ----
@app.get("/")
def root():
    return {"message": "Habit Tracker API is running 🚀"}

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

# ---- Railway / Cloud entry point ----
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
