from fastapi import APIRouter

from app.schemas.interview import (
    InterviewAnswerRequest,
    InterviewAnswerResponse,
    InterviewStartRequest,
    InterviewStartResponse,
)
from app.services.interview_service import InterviewService


router = APIRouter()
interview_service = InterviewService()


@router.post("/start", response_model=InterviewStartResponse)
def start_interview(data: InterviewStartRequest):
    return interview_service.start_interview(data)


@router.post("/answer", response_model=InterviewAnswerResponse)
def submit_answer(data: InterviewAnswerRequest):
    return interview_service.submit_answer(data)
