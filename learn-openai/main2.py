from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)

res = client.chat.completions.create(
    model="google/gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "always answer in emojis"},
        {"role": "user", "content": "Draw me the phase of life!"},
    ],
    extra_body={"reasoning": {"enabled": True}},
)

result = res.choices[0].message.content
print(result)
