from fastapi import APIRouter
from app.schemas.question import QuestionGenerateRequest, QuestionGenerateResponse
from app.services.question_service import QuestionService

router=APIRouter()
question_service=QuestionService()

@router.post("/generate", response_model=QuestionGenerateResponse)
def generate_questions(data: QuestionGenerateRequest):
    return question_service.generate_questions(data)