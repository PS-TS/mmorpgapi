from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler

from src.api.routers.item import router as item_router
from src.api.routers.inventory import router as inventory_router
from src.api.routers.player import router as player_router
from src.api.routers.user import router as user_router
from src.container import Container
from src.db import database, init_db

container = Container()
container.wire(modules=[
    "src.api.routers.item", 
    "src.api.routers.inventory",
    "src.api.routers.player",
    "src.api.routers.user",
])


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    """Funkcja żywotności działająca przy uruchomieniu aplikacji"""
    await init_db()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(item_router, prefix="/item")
app.include_router(inventory_router, prefix="/inventory")
app.include_router(player_router, prefix="/player")
app.include_router(user_router, prefix="/user")

@app.exception_handler(HTTPException)
async def http_exception_handle_logging(
    request: Request,
    exception: HTTPException,
) -> Response:
    """Funkcja obsługująca wyjątki http na potrzeby logowania.

    Args:
        request (Request): Żądanie http
        exception (HTTPException): Wyjątek

    Returns:
        Response: Odpowiedź http
    """
    return await http_exception_handler(request, exception)
