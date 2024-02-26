# database_initializer.py
from config.database import SessionLocal, engine, Base
from models.role import Role
from models.users import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar la base de datos con roles y usuarios al iniciar la aplicación
def init_db():
    db = SessionLocal()
    try:
        roles = ["Usuario", "Admin", "Autor", "Confirmador"]

        for role_name in roles:
            try:
                role = Role(name=role_name)
                db.add(role)
                db.commit()
            except IntegrityError:
                db.rollback()

        users_data = [
            {"username": "usuario1", "email": "usuario1@example.com", "password": "password1", "role_name": "Usuario"},
            {"username": "admin1", "email": "admin1@example.com", "password": "password2", "role_name": "Admin"},
            {"username": "autor1", "email": "autor1@example.com", "password": "password3", "role_name": "Autor"},
            {"username": "confirmador1", "email": "confirmador1@example.com", "password": "password4", "role_name": "Confirmador"},
        ]

        for user_data in users_data:
            role_name = user_data.pop("role_name")
            role = db.query(Role).filter(Role.name == role_name).first()
            if role:
                existing_user = db.query(User).filter(User.username == user_data["username"]).first()
                if not existing_user:
                    user_data["role"] = role
                    user = User(**user_data)
                    db.add(user)

        db.commit()

    finally:
        db.close()