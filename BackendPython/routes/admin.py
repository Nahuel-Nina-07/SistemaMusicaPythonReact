from fastapi import APIRouter, Depends, HTTPException, status
from config.db_utils import *
import models, schemas

router = APIRouter()

@router.get("/users/", status_code=status.HTTP_200_OK)
async def Listar_Usuarios(db:db_dependency):
    registro=db.query(models.users.User).all()
    return registro
