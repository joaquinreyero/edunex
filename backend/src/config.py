from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
import sentry_sdk

from src.models.models import Base

import os


def configure_cors(app: FastAPI):
    origins = [
        "http://localhost:8080",
    ]
    app.add_middleware(
        CORSMiddleware,
        #allow_origins=origins,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def configure_sentry(app: FastAPI):
    sentry_sdk.init(
        dsn=Settings.DSN_SENTRY,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )
    app.add_middleware(SentryAsgiMiddleware)


class Settings:

    DATABASE_URI = os.getenv("DATABASE_URI_LOCAL")
    DSN_SENTRY = os.getenv("DSN_SENTRY")


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(Settings.DATABASE_URI)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

settings = Settings()