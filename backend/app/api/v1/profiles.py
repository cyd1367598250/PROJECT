from fastapi import APIRouter
from app.schemas.profile import ProfileCreate,ProfileAnalysis
from app.services.profile_service import ProfileService

router=APIRouter()
profile_service=ProfileService()

@router.post("/analyze",response_model=ProfileAnalysis)
def analyze_profile(data:ProfileCreate):
    return profile_service.analyze_profile(data)