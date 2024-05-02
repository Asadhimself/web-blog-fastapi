from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base
from api.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def includer_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
    create_tables()
    includer_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
