import requests

proxy = "http://h496QE:7YH3NP@38.170.252.141:9057"
proxies = {
    "http": proxy,
    "https": proxy,
}

r = requests.post("https://api.openai.com/v1/chat/completions", headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
}, json={
    "model": "gpt-3.5-turbo-0125",
    "messages": [{"role": "user", "content": "What is the OpenAI mission?"}]
}, proxies=proxies)

print(r.json())
