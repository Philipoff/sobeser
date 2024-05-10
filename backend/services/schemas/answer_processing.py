from pydantic import BaseModel


class QAModel(BaseModel):
    question: str
    answer: str
