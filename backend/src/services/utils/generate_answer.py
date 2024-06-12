from ...services.utils.gemini import gemini_search
from ...services.utils.chatgpt import chatgpt_35_turbo_QA
from random import random


def generate_answer(question, answer):
    if random() <= 0.5:
        answer = gemini_search(question, answer)
        model = "gemini"
    else:
        if len(question + answer) > 400:
            model = "ChatGPT 16k"
            answer = chatgpt_35_turbo_QA(question, answer, "16k")
        else:
            model = "ChatGPT 16k"
            answer = chatgpt_35_turbo_QA(question, answer, "4k")
    return {
        "answer": answer,
        "model": model
    }
