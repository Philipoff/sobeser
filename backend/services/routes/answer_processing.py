from fastapi import APIRouter
from random import random
from backend.services.utils.gemini import gemini_search
from backend.services.utils.chatgpt import chatgpt_35_turbo_QA
from backend.services.schemas.answer_processing import QAModel
from time import sleep

QA_router = APIRouter(
    tags=["QA"],
    responses={404: {"description": "Not found"}},
)


# @QA_router.get("/check_answer/{task_id}")
# def get_status(task_id):
#     return task_id


@QA_router.post("/check_answer")
async def check_answer(form: QAModel):
    try:
        if random() <= 0.5:
            answer = gemini_search(form.question, form.answer)
        else:
            if len(form.question + form.answer) > 400:
                answer = chatgpt_35_turbo_QA(form.question, form.answer, "16k")
            else:
                answer = chatgpt_35_turbo_QA(form.question, form.answer, "4k")
    except Exception as e:
        print(e)
        answer = "Technical error. Try again"
    return answer


if __name__ == "__main__":
    print(gemini_search("How to create a list in Python?", "list = [1, 2, 3]"))
