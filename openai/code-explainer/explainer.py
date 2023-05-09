import os
from functools import partial

import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

def send_question(question: str) -> dict:
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a developer."},
            {"role": "user", "content": question},
        ],
    )


def retrieve_ai_answer(response: dict) -> str:
    return response["choices"][0]["message"]["content"]


def get_code_info(question: str, code: str) -> str:
    resp = send_question(f"{question}\n\n{code}")
    return retrieve_ai_answer(resp)


retrieve_code_language = partial(
    get_code_info,
    question="Can you tell me what language this code is written in with one word?",
)

retrieve_code_explanation = partial(
    get_code_info,
    question="Can you explain what this code does in one paragraph?",
)

if __name__=="__main__":
    lang = get_code_info("Can you tell me what language this code is written in with one word?", "print('hello')")
    print(lang)