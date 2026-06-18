from fastapi import APIRouter
from app.api.v1 import interviews, profiles, progress, questions, reviews

api_router = APIRouter()

api_router.include_router(
    profiles.router,
    prefix="/v1/profiles",
    tags=["profiles"],
)

api_router.include_router(
    questions.router,
    prefix="/v1/questions",
    tags=["questions"],
)

api_router.include_router(
    interviews.router,
    prefix="/v1/interviews",
    tags=["interviews"],
)

api_router.include_router(
    reviews.router,
    prefix="/v1/reviews",
    tags=["reviews"],
)

api_router.include_router(
    progress.router,
    prefix="/v1/progress",
    tags=["progress"],
)