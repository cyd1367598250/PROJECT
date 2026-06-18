from fastapi import APIRouter

from app.schemas.review import AnswerReviewRequest, AnswerReviewResponse
from app.services.review_service import ReviewService

router =APIRouter()
review_service=ReviewService()

@router.post("/answer", response_model=AnswerReviewResponse)
def review_answer(data: AnswerReviewRequest):
    return review_service.review_answer(data)

