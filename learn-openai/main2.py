from openai import OpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field

load_dotenv()

class Activity(BaseModel):
    time: str = Field(description="Between Morning, Afternoon, Evening")
    activity: str = Field(description="The description of the activity")
    location: str = Field(description="The location of the activity")

class Itenerary(BaseModel):
    city: str = Field(description="The city name")
    days: int = Field(description="The number of days to stay in the city")
    budget: int = Field(description="The budget for the trip in USD")
    activities: list[Activity] = Field(description="The list of activities to do in the city")


client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1")

user_input = """
    Destination CIty: Seoul, South Korea
    Days of stay: 3 days
    Budget: USD 250 per day
    """

res = client.chat.completions.parse(
    model="google/gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "Generate a travel itenerary based on user context"},
        {"role": "user", "content": user_input},
    ],
    extra_body={"reasoning": {"enabled": True}},
    response_format=Itenerary
)

result = res.choices[0].message.parsed
print(result)
