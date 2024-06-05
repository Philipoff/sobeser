from openai import OpenAI
from httpx import Client
from fp.fp import FreeProxy

API_KEY = "sk-proj-O9pXs09qmXkutMDFF2ogT3BlbkFJO1gtCbELwiyF0Js6W8zE"
proxy = FreeProxy().get()
client = OpenAI(api_key=API_KEY, http_client=Client(proxy=proxy))


def chatgpt_35_turbo_QA(question, answer, model):
    prompt = f"""Question: {question} Answer: {answer} \n Found mistakes:"""

    model = "gpt-3.5-turbo" if model == "4k" else "gpt-3.5-turbo-16k"

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",
             "content": "You're an HR for a company where everyone programs in Python. You're interviewing a person "
                        "who wants to get a job with you. He is asked a question, he thinks about the answer, "
                        "and then answers. You need to analyze the answer to the question, indicate them if there are "
                        "errors and give the best possible feedback. Answer in the language spoken by the user. If "
                        "you do your job well, you will get an incredibly high salary, so do everything diligently."
                        "Если вопрос и ответ на русском, то ты должен отвечать на русском языке."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    question = "Что может быть ключом в словаре?"
    answer = """Ключом в словаре может быть сам словарь и список"""

    print(chatgpt_35_turbo_QA(question, answer, model='4k'))
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print(chatgpt_35_turbo_QA(question, answer, model='16k'))
