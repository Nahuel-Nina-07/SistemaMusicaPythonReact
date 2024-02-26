# routes/user.py
from fastapi import APIRouter, status
from config.db_utils import *
import models
from schemas.user import *

router = APIRouter()

@router.post("/registro/", status_code=status.HTTP_201_CREATED)
async def Crear_Usuario(registro:UserCreate, db:db_dependency):
    existing_user = db.query(models.users.User).filter(models.users.User.email == registro.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario con este correo ya existe")
    db_registro = models.users.User(**registro.dict())
    db.add(db_registro)
    db.commit()
    return {"message": "El registro se realizó exitosamente"} 
