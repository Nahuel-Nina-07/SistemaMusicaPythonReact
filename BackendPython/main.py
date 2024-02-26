# main.py
from fastapi import FastAPI
from config.db_initializer import init_db
from routes.user import router as user_router
from routes.admin import router as admin_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin={
    "http://localhost:5173",
}
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Inicializar la base de datos al iniciar la aplicación
init_db()

# Incluir las rutas de usuario
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])
