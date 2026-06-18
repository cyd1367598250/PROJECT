from app.schemas.profile import ProfileCreate, ProfileAnalysis

class ProfileService:
    def analyze_profile(self,data:ProfileCreate) -> ProfileAnalysis:
        level=self._infer_level(data.experience_years)
        strengths=[]
        weaknesses=[]
        focus_area=[]

        if data.skills:
            strengths.append(f"已有技能基础：{','.join(data.skills)}")        
        else:
            weaknesses.append("技能信息不足，需要补充技术栈或能力标签")

        if data.experience_years<1:
            focus_area.extend(["基础知识","项目表达","实习/校园经历包装"])
        elif data.experience_years<=3:
            focus_area.extend(["项目深挖","技术原理","业务理解"])
        else:
            focus_area.extend(["系统设计","团队协作","复杂问题解决"])

        return ProfileAnalysis(
            target_position=data.target_position,
            level=level,
            strengths=strengths,
            weaknesses=weaknesses,
            suggested_focus_areas=focus_area,
            summary=f"用户目标岗位为{data.target_position}，当前处于{level}水平，建议优先准备{','.join(focus_area)}。",
        )
    
    def _infer_level(self,experience_years:int)->str:
        if experience_years<1:
            return "入门/校招"
        if experience_years<=3:
            return "初级/中级"
        if experience_years<=5:
            return "中高级"
        return "高级"