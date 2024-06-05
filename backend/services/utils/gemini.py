import requests
from fp.fp import FreeProxy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

proxy = FreeProxy().get()
proxies = {
    "http": proxy,
    "https": proxy,
}


def gemini_search(question, answer, temperature=0.1):
    API_KEY = "AIzaSyBirO5FrDHTWlVKdMBv0rzzwGLRa0kUkIY"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-pro-latest:generateContent?key={API_KEY}"
    prompt = f"""Question: {question} Answer: {answer} \n Found mistakes:"""

    request_body = {
        "contents": [{
            "role": "model",
            "parts": [
                {"text": "You're an HR for a company where everyone programs in Python. You're interviewing a person "
                         "who wants to get a job with you. He is asked a question, he thinks about the answer, "
                         "and then answers. You need to analyze the answer to the question, indicate them if there are "
                         "errors and give the best possible feedback. Answer in the language spoken by the user. If "
                         "you do your job well, you will get an incredibly high salary, so do everything diligently"
                         "Если вопрос и ответ на русском, то ты должен отвечать на русском языке."}],
        }, {
            "role": "user",
            "parts": [{"text": prompt}],
        }],
        "generationConfig": {
            "temperature": temperature,
        },
    }
    r = requests.post(url, json=request_body, proxies=proxies)
    if r.status_code == 200:
        return r.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text")
    return False


if __name__ == "__main__":
    question = "Что может быть ключом в словаре?"
    answer = """Ключом в словаре может быть сам словарь и список"""

    print(gemini_search(question, answer))
