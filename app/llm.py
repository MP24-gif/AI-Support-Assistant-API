
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY is not configured")

client = Groq(
    api_key=api_key,
    timeout=20.0,
)


def ask_model(question: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an IT support assistant. "
                    "Give accurate, practical troubleshooting guidance. "
                    "Start with the 3 to 5 most useful steps. "
                    "Use numbered instructions and simple language. "
                    "Ask a clarifying question when important details are missing. "
                    "Do not invent company-specific policies. "
                    "Do not recommend disabling security software or performing "
                    "destructive system changes unless necessary and clearly explained."
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content

    if not answer:
        raise RuntimeError("The AI model returned an empty response.")

    return answer
