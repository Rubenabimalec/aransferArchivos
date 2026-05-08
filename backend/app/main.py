from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config import settings
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Crear carpeta de uploads si no existe
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    yield


app = FastAPI(
    title="FileDrop API",
    description="Servicio de transferencia de archivos",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}