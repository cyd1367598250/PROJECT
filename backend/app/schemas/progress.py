from pydantic import BaseModel, Field

class ProgressAdviceRequest(BaseModel):
    company: str = Field(..., description="面试公司")
    target_position: str = Field(..., description="面试岗位")
    round_name: str = Field(..., description="面试轮次")
    status: str = Field(..., description="面试状态")
    asked_questions: list[str] = Field(default_factory=list, description="面试中被问到的问题")
    weak_points: list[str] = Field(default_factory=list, description="用户觉得薄弱的地方")
    next_round_date: str | None = Field(default=None, description="下一轮面试日期")

class ProgressAdviceResponse(BaseModel):
    summary:str
    next_focus_areas:list[str]
    suggested_actions:list[str]
    risk_level:str