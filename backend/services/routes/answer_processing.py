from fastapi import APIRouter
from backend.services.utils.gemini import gemini_search
from backend.services.schemas.gemini import QAModel

QA_router = APIRouter(
    tags=["QA"],
    responses={404: {"description": "Not found"}},
)


@QA_router.post("/api/check_answer")
async def check_answer(form: QAModel):
    gemini_answer = gemini_search(form.question, form.answer)
    return gemini_answer


if __name__ == "__main__":
    print(gemini_search("How to create a list in Python?", "list = [1, 2, 3]"))
