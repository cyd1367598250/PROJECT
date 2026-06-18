from pydantic import BaseModel,Field

class ProfileCreate(BaseModel):
    target_position: str=Field(..., description="意向岗位")
    experience_years: int=Field(...,ge=0,description="工作年限")
    skills: list[str]=Field(default_factory=list,description="技能列表")
    target_companies: list[str]=Field(default_factory=list,description="目标公司")
    self_summary:str|None=Field(default=None,description="个人情况描述")

class ProfileAnalysis(BaseModel):
    target_position: str
    level: str
    strengths: list[str]
    weaknesses: list[str]
    suggested_focus_areas: list[str]
    summary: str 

#用户请求接口时，需要传入相应信息，ProfileCreate
# ProfileAnalysis是返回格式
  