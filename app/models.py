from pydantic import BaseModel, Field


class SupportRequest(BaseModel):
    question: str = Field(
        min_length=10,
        max_length=1000,
        description="IT support question"
    )


class SupportResponse(BaseModel):
    success: bool
    question: str
    answer: str