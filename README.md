# 📌 FastAPI Todo CRUD Application

A simple and clean **CRUD REST API** built with **FastAPI**, **SQLAlchemy**, and **SQLite**.  
This project is perfect for learning FastAPI fundamentals — dependency injection, database models, Pydantic schemas, routing, and proper CRUD patterns.

---

## 🚀 Features

- Create Todo
- Read all Todos
- Read single Todo by ID
- Update Todo
- Delete Todo
- Auto-handled timestamps (`created_at`, `updated_at`)
- Request validation using **Pydantic**
- Clean database session management using `Depends`

---

## 📂 Project Structure

fastapi_todo/
│── main.py # All routes and CRUD logic
│── model.py # SQLAlchemy models (Todos)
│── schemas.py # Pydantic request/response schemas
│── database.py # DB engine, SessionLocal, Base
│── requirements.txt # Dependencies
│── todo.db # SQLite database (auto-created)


---

## 🛠️ Technologies Used

- **FastAPI** – Web framework
- **SQLAlchemy ORM** – Database layer
- **SQLite** – Lightweight database
- **Pydantic** – Data validation
- **Uvicorn** – Development server

---

## ⚙️ Installation & Running the Project

### 1️⃣ Create virtual environment (recommended)
```sh
python -m venv venv


2️⃣ Activate environment
```sh
venv\Scripts\activate


3️⃣ Install dependencies
```sh
pip install -r requirements.txt

4️⃣ Run the FastAPI server
```sh
uvicorn main:app --reload



✔️ Conclusion

This project is a perfect starting point to understand how a real backend works with FastAPI + SQLAlchemy. Everything is clean and modular, so revisiting this later will be easy.