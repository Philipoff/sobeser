import openai
from fastapi import APIRouter
from ...services.utils.generate_answer import generate_answer
from ...services.schemas.answer_processing import QAModel

QA_router = APIRouter(
    tags=["QA"],
    responses={404: {"description": "Not found"}},
)


# @QA_router.get("/check_answer/{task_id}")
# def get_status(task_id):
#     return task_id


@QA_router.post("/check_answer")
async def check_answer(form: QAModel):
    answer = None
    while not answer:
        try:
            answer = generate_answer(form.question, form.answer)["answer"]
        except openai.APIConnectionError:
            pass
    return answer


if __name__ == "__main__":
    print(generate_answer("How to create a list in Python?", "list = [1, 2, 3]"))
