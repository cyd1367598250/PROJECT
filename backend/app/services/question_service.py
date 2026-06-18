from app.schemas.question import(
    QuestionGenerateRequest,
    QuestionGenerateResponse,
    InterviewQuestion,
)

class QuestionService:
    def generate_questions(
        self,
        data:QuestionGenerateRequest,
    )->QuestionGenerateResponse:
        questions: list[InterviewQuestion]=[]
        questions.extend(self._generate_common_questions(data))
        questions.extend(self._generate_skill_questions(data))
        questions.extend(self._generate_project_questions(data))

        return QuestionGenerateResponse(
            target_position=data.target_position,
            questions=questions,
        )

    def _generate_common_questions(
        self,
        data: QuestionGenerateRequest,
    ) ->list[InterviewQuestion]:
        return[
            InterviewQuestion(
                question=f"请你简单介绍一下自己，以及为什么想应聘{data.target_position}？",
                category="通用问题",
                difficulty="简单",
                reason="用于考察候选人的表达能力、岗位动机和基本匹配度。",
            ),
            InterviewQuestion(
                question="请介绍一个你最有代表性的项目，你在其中负责什么？",
                category="项目问题",
                difficulty="中等",
                reason="用于引导候选人展示项目经验和个人贡献。",
            ),
        ]
    
    def _generate_skill_questions(
        self,
        data:QuestionGenerateRequest,
    )->list[InterviewQuestion]:
        questions=[]

        for skill in data.skills[:5]:
            questions.append(
                InterviewQuestion(
                    question=f"你在项目中是如何使用 {skill} 的？有没有遇到过什么问题？",
                    category="技术问题",
                    difficulty="中等",
                    reason=f"用户填写了 {skill}，需要验证其真实掌握程度和项目应用能力。",
                )
            )
        
        if not questions:
            questions.append(
                InterviewQuestion(
                    question="你目前最熟悉的技术或工具是什么？请结合项目说明。",
                    category="技术问题",
                    difficulty="简单",
                    reason="用户暂未填写技能，需要先补充技术画像。",
                )
            )
        return questions
    
    def _generate_project_questions(
        self,
        data: QuestionGenerateRequest,
    ) -> list[InterviewQuestion]:
        if data.experience_years < 1:
            return [
                InterviewQuestion(
                    question="你做过哪些课程项目、实习项目或个人项目？请详细介绍一个。",
                    category="项目问题",
                    difficulty="简单",
                    reason="校招或入门用户需要重点训练项目表达。",
                )
            ]

        if data.experience_years <= 3:
            return [
                InterviewQuestion(
                    question="你负责的项目中，技术难点是什么？你是怎么解决的？",
                    category="项目深挖",
                    difficulty="中等",
                    reason="1-3 年经验需要重点考察项目深度和问题解决能力。",
                )
            ]

        return [
            InterviewQuestion(
                question="请你设计一个高并发场景下的核心业务系统，并说明架构取舍。",
                category="系统设计",
                difficulty="困难",
                reason="高年限候选人需要考察系统设计和架构能力。",
            )
        ]