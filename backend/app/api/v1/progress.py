from fastapi import APIRouter

from app.schemas.progress import ProgressAdviceRequest, ProgressAdviceResponse
from app.services.progress_service import ProgressService

from fastapi import APIRouter

from app.schemas.progress import ProgressAdviceRequest, ProgressAdviceResponse
from app.services.progress_service import ProgressService


router = APIRouter()
progress_service = ProgressService()


@router.post("/advice", response_model=ProgressAdviceResponse)
def generate_progress_advice(data: ProgressAdviceRequest):
    return progress_service.generate_advice(data)