from pydantic import BaseModel, Field

class AnswerReviewRequest(BaseModel):
    question: str = Field(..., description="面试题")
    answer: str = Field(..., description="用户回答")
    target_position: str = Field(..., description="意向岗位")

class AnswerReviewResponse(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    improved_answer: str
    summary: str