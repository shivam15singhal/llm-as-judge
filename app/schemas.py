from pydantic import BaseModel


class CriterionScore(BaseModel):

    score: int

    rationale: str


class JudgeVerdict(BaseModel):

    correctness: CriterionScore

    faithfulness: CriterionScore

    completeness: CriterionScore

    instruction_following: CriterionScore

    tone_safety: CriterionScore

    overall_score: float

    pass_case: bool

    summary: str