from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables

from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Tables created")
    yield
    await delete_tables()
    print("Tables deleted")


app = FastAPI(lifespan=lifespan)


app.include_router(task_router)
