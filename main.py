from fastapi import FastAPI

from api.routers.books import router as book_router
from api.routers.users import router as user_router
from api.routers.lends import router as lend_router

app = FastAPI()

app.include_router(book_router, prefix="/book")
app.include_router(user_router, prefix="/user")
app.include_router(lend_router, prefix="/lend")