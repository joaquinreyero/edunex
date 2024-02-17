from fastapi import FastAPI

from src.api import health, university, degree, subject
from src.config import configure_cors, configure_sentry

app = FastAPI()

configure_cors(app)
configure_sentry(app)

app.include_router(health.router)
app.include_router(university.router)
app.include_router(degree.router)
app.include_router(subject.router)
