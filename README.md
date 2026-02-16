🧠 User CRUD – Backend Logic Practice
📌 Why I Built This

I built this project to strengthen my backend fundamentals.

Instead of jumping straight into frameworks, I wanted to deeply understand how a real backend works internally — especially:

CRUD operations

Business rules

Data validation

State management

Logical flow of backend systems

This project simulates what happens behind an API before adding frameworks like FastAPI or databases.

🛠 What This Project Does

It simulates a User Management System using pure Python.

The system allows:

Create users

List users

Update users

Delete users

All data is stored in memory (list of dictionaries), simulating a simple database.

🧠 What I Focused On

Instead of just making it “work”, I focused on:

Preventing duplicate emails

Validating password length

Ensuring unique IDs

Returning clear responses

Separating logic into functions

I wanted to think like a backend developer, not just a Python learner.

📂 Project Structure
user-crud/
│
├── main.py
└── README.md


Simple structure on purpose.
The goal here was logic clarity, not complexity.

🔎 Example Logic (Create User)
def criar_usuario(usuarios, nome, email, senha):

    if len(senha) < 6:
        return "Error: password too short"

    for usuario in usuarios:
        if usuario["email"] == email:
            return "Error: email already exists"

    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": nome,
        "email": email,
        "senha": senha
    }

    usuarios.append(novo_usuario)

    return "User created successfully"

💡 What This Project Represents

This is the logical foundation behind:

REST APIs

Authentication systems

Real backend services

Framework-based applications

Before using FastAPI, Django, or databases, I wanted to fully understand what happens underneath.

🚀 Next Improvements

This project is intentionally simple, but my next steps are:

Add password hashing

Implement login system

Convert into a FastAPI REST API

Connect to SQLite/PostgreSQL

Add JWT authentication

Write unit tests

👨‍💻 About Me

I'm currently focused on backend development, studying:

Python

API design

Authentication systems

Clean code principles

Backend architecture fundamentals

This project is part of my journey to build strong backend foundations before moving into more complex systems.
