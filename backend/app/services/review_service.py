from app.schemas.review import AnswerReviewRequest, AnswerReviewResponse

class ReviewService:
    def review_answer(self,data:AnswerReviewRequest) -> AnswerReviewResponse:
        score=self._calculate_score(data.answer)
        strengths=self._find_strengths(data.answer)
        weaknesses=self._find_weaknesses(data.answer)
        improved_answer=self._build_improved_answer(data)

        return AnswerReviewResponse(
            score=score,
            strengths=strengths,
            weaknesses=weaknesses,
            improved_answer=improved_answer,
            summary=f"这份回答当前评分为 {score}/10，建议继续补充细节、结果和复盘。",
        )
    
    def _calculate_score(self,answer:str)->int:
        answer_length=len(answer.strip())

        if answer_length<30:
            return 4
        if answer_length<80:
            return 6
        if answer_length<150:
            return 7
        return 8
    
    def _find_strengths(self, answer: str) -> list[str]:
        strengths = []

        if len(answer.strip()) >= 80:
            strengths.append("回答有一定信息量，能够展开说明。")

        if "项目" in answer:
            strengths.append("回答中提到了项目经历，具备进一步深挖空间。")

        if not strengths:
            strengths.append("回答已经开始回应问题，但还需要补充更多具体内容。")

        return strengths
    
    def _find_weaknesses(self, answer: str) -> list[str]:
        weaknesses = []

        if len(answer.strip()) < 80:
            weaknesses.append("回答偏短，信息量不足。")

        if "结果" not in answer and "提升" not in answer and "优化" not in answer:
            weaknesses.append("缺少结果表达，建议补充量化成果或业务价值。")

        if "反思" not in answer and "复盘" not in answer:
            weaknesses.append("缺少复盘思考，建议说明你从经历中学到了什么。")

        return weaknesses
    
    def _build_improved_answer(self, data: AnswerReviewRequest) -> str:
        return (
            f"针对「{data.question}」，可以这样组织回答："
            f"我在准备{data.target_position}岗位时，会先说明背景，"
            "再说明我具体负责的任务、采取的行动、最终结果，以及这段经历带来的复盘。"
            "如果结合真实项目，建议补充技术难点、解决方案和量化收益。"
        )