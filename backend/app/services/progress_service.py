from app.schemas.progress import ProgressAdviceRequest, ProgressAdviceResponse

class ProgressService:
    def generate_advice(self,data: ProgressAdviceRequest)->ProgressAdviceResponse:
        next_focus_areas=self._build_focus_areas(data)
        suggested_actions=self._build_suggested_actions(data)
        risk_level=self._infer_risk_level(data)

        return ProgressAdviceResponse(
            summary=self._build_summary(data, next_focus_areas),
            next_focus_areas=next_focus_areas,
            suggested_actions=suggested_actions,
            risk_level=risk_level,
        )
    
    def _build_focus_areas(self, data: ProgressAdviceRequest) -> list[str]:
        focus_areas:list[str]=[]
        all_text = " ".join(data.asked_questions + data.weak_points)
        if "Redis" in all_text or "缓存" in all_text:
            focus_areas.append("Redis 与缓存机制")
        
        if "项目" in all_text or "权限" in all_text:
            focus_areas.append("项目深挖与职责表达")
        
        if "系统设计" in all_text or "高并发" in all_text:
            focus_areas.append("系统设计与架构取舍")
        
        if "算法" in all_text:
            focus_areas.append("算法与数据结构")

        if not focus_areas:
            focus_areas.append("通用面试表达与岗位匹配度")

        return focus_areas

    def _build_suggested_actions(self, data: ProgressAdviceRequest) -> list[str]:
        actions: list[str]=[]

        all_text=" ".join(data.asked_questions+data.weak_points)

        if "Redis" in all_text or "缓存" in all_text:
            actions.append("整理 Redis 高频问题，包括缓存穿透、缓存击穿、缓存雪崩和数据一致性。")
        
        if "项目" in all_text or "权限" in all_text:
            actions.append("重新整理一个核心项目，按背景、职责、难点、方案、结果、复盘来表达。")
        
        if "系统设计" in all_text or "高并发" in all_text:
            actions.append("准备一个高并发场景的系统设计案例，重点说明架构取舍。")

        if "算法" in all_text:
            actions.append("每天练习 2-3 道岗位相关算法题，并总结解题思路。")

        if data.next_round_date:
            actions.append(f"下一轮面试日期是 {data.next_round_date}，建议提前完成重点问题复盘。")
        
        if not actions:
            actions.append("复盘本轮被问到的问题，整理成问题、原回答、优化回答三列。")
    
    def _infer_risk_level(self, data: ProgressAdviceRequest) -> str:
        if data.status =="failed":
            return "high"

        if len(data.weak_points)>=3:
            return "high"
        
        if len(data.weak_points)>=1 or len(data.asked_questions)>=4:
            return "medium"
        
        return "low"
    
    def _build_summary(
        self,
        data: ProgressAdviceRequest,
        next_focus_areas: list[str],
    ) -> str:
        focus_text = "、".join(next_focus_areas)

        return (
            f"你在 {data.company} 的 {data.round_name} 面试中，"
            f"目标岗位是 {data.target_position}。"
            f"根据本轮记录，下一步建议重点准备：{focus_text}。"
        )