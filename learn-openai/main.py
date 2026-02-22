from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1")

SYSTEM_PROMPT = """
You are great story teller, and you craft good short story for kids based on user Input.

<example_output>
# Story Title

story content - maksimum 3 paragraph

> The wisdom for kids
</example_output>

<guidelines>
- Use Bahasa Indonesia to craft the story
- Make sure it's easy to understand for kids
</guidelines>

<guardrails>
- Do not use any harms scenario
- Do not use any violence or sexual content
- Do not use any hate speach or discrimination
</guardrails>
"""

res = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "A friendship of Deer and a Rabbit in the Jungle"},
    ],
    extra_body={"reasoning": {"enabled": True}},
)

result = res.choices[0].message.content
print(result)
