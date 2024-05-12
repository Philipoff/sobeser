import requests

proxy = "http://h496QE:7YH3NP@38.170.252.141:9057"
proxies = {
    "http": proxy,
    "https": proxy,
}


def gemini_search(question, answer, temperature=0.1):
    API_KEY = "AIzaSyBirO5FrDHTWlVKdMBv0rzzwGLRa0kUkIY"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={API_KEY}"
    request_body = {
        "contents": [{
            "role": "model",
            "parts": [
                {"text": """You are an interviewer in IT company. Check the answer in programming question and find 
                mistakes in it. Give a good feedback about this question"""}],
        }, {
            "role": "user",
            "parts": [{"text": f"Question: {question}\n Answer: {answer}"}],
        }],
        "generationConfig": {
            "temperature": temperature,
        },
    }
    r = requests.post(url, json=request_body, proxies=proxies)
    if r.status_code == 200:
        return r.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text").replace("\n", '<br>')
    return False
