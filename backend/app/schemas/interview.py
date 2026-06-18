from pydantic import BaseModel, Field


class InterviewStartRequest(BaseModel):
    target_position: str = Field(..., description="意向岗位")
    interview_type: str = Field(default="technical", description="面试类型")
    difficulty: str = Field(default="medium", description="面试难度")


class InterviewStartResponse(BaseModel):
    opening_message: str
    first_question: str
    interview_type: str
    difficulty: str


class InterviewAnswerRequest(BaseModel):
    question: str = Field(..., description="当前面试题")
    answer: str = Field(..., description="用户回答")
    target_position: str = Field(..., description="意向岗位")


class InterviewAnswerResponse(BaseModel):
    feedback: str
    follow_up_question: str
    suggested_improvement: str
