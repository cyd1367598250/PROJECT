from pydantic import BaseModel,Field

class QuestionGenerateRequest(BaseModel):
    target_position:str=Field(...,description="意向岗位")
    experience_years: int=Field(...,ge=0,description="工作年限")
    skills:list[str]=Field(default_factory=list,description="技能列表")
    focus_areas: list[str]=Field(default_factory=list,description="重点准备方向")

class InterviewQuestion(BaseModel):
    question: str
    category: str
    difficulty: str
    reason: str

class QuestionGenerateResponse(BaseModel):
    target_position: str
    questions: list[InterviewQuestion]