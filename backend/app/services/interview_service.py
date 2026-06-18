from app.schemas.interview import (
    InterviewAnswerRequest,
    InterviewAnswerResponse,
    InterviewStartRequest,
    InterviewStartResponse,
)


class InterviewService:
    def start_interview(self, data: InterviewStartRequest) -> InterviewStartResponse:
        first_question = self._build_first_question(data.target_position, data.interview_type)

        return InterviewStartResponse(
            opening_message=f"你好，我们开始一场{data.target_position}的模拟面试。",
            first_question=first_question,
            interview_type=data.interview_type,
            difficulty=data.difficulty,
        )

    def submit_answer(self, data: InterviewAnswerRequest) -> InterviewAnswerResponse:
        feedback = self._review_answer(data.answer)
        follow_up_question = self._build_follow_up_question(data)

        return InterviewAnswerResponse(
            feedback=feedback,
            follow_up_question=follow_up_question,
            suggested_improvement="建议回答时补充背景、你的具体行动、最终结果和复盘思考。",
        )

    def _build_first_question(self, target_position: str, interview_type: str) -> str:
        if interview_type == "project":
            return "请介绍一个你最有代表性的项目，并说明你负责的核心部分。"
        if interview_type == "hr":
            return f"你为什么想应聘{target_position}这个岗位？"
        return f"请你先简单介绍一下自己，以及你和{target_position}岗位的匹配点。"

    def _review_answer(self, answer: str) -> str:
        if len(answer.strip()) < 30:
            return "你的回答偏短，目前信息量不够，建议补充项目背景、个人职责和具体结果。"
        if len(answer.strip()) < 100:
            return "你的回答已经有基本内容，但还可以进一步补充细节和量化结果。"
        return "你的回答比较完整，接下来可以继续加强技术细节、难点拆解和结果表达。"

    def _build_follow_up_question(self, data: InterviewAnswerRequest) -> str:
        if "项目" in data.question:
            return "这个项目里最大的技术难点是什么？你当时是怎么分析和解决的？"
        if "为什么" in data.question:
            return "你能结合自己的经历，说明为什么这个岗位适合你吗？"
        return "如果面试官继续追问，你会如何用一个具体案例证明你的能力？"
