from fastapi import FastAPI
from prisma import Prisma
from contextlib import asynccontextmanager
from app.routers.auth import auth

prisma = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    if prisma.is_connected:
        prisma.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(auth)
