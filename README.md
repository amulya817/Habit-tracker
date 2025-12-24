# Habit Tracker – Full Stack Web Application 🌱

A simple and elegant full-stack Habit Tracker application that allows users to create, track, and manage daily habits. The project demonstrates end-to-end development, from backend API design to frontend UI and cloud deployment.

---

## 🔗 Live Demo

- **Frontend (Vercel)**:(https://habit-tracker-two-beryl.vercel.app/)
---**backend(Railways)**

## 🛠 Tech Stack

### Frontend
- React (Create React App)
- HTML, CSS
- JavaScript (ES6)
- Deployed on **Vercel**

### Backend
- FastAPI (Python)
- RESTful API design
- Uvicorn ASGI server
- Deployed on **Railway**

---

## ✨ Features

- Add new habits
- Mark habits as completed
- Delete habits
- Real-time frontend–backend communication
- REST API with Swagger documentation
- Fully deployed and accessible online

---

## 📂 Project Structure

Habit-tracker/
├── backend/
│ ├── main.py
│ ├── requirements.txt
│ └── .gitignore
│
├── frontend/
│ └── habit-frontend/
│ ├── src/
│ ├── public/
│ └── package.json
│
└── README.md


---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/habits` | Fetch all habits |
| POST | `/habits` | Add a new habit |
| PUT | `/habits/{id}` | Toggle habit completion |
| DELETE | `/habits/{id}` | Delete a habit |

Swagger UI available at:
/docs

---

## 🧪 Run Locally

### Backend
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Frontend
cd frontend/habit-frontend
npm install
npm start
```
🌍 Deployment
Frontend: Vercel

Backend: Railway

Environment-ready with dynamic port handling

📌 Learning Outcomes
Full-stack application architecture

REST API development using FastAPI

Frontend–backend integration

Cloud deployment (Vercel & Railway)

Git version control and deployment workflows

👩‍💻 Author
Amulya B
Final Year Engineering Student (AI & ML)
GitHub: https://github.com/amulya817

📄 License
This project is for learning and portfolio purposes.
