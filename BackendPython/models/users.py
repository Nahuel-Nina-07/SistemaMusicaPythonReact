# models/users.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from models.role import Role 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    id_role = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role', back_populates='users')