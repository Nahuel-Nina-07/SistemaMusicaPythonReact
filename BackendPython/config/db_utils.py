from typing import Annotated
from config.database import SessionLocal, engine
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]