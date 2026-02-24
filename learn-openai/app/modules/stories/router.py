from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from .prompt import SYSTEM_PROMPT
from app.utils.openai import client
import markdown

template = Jinja2Templates("templates")
stories_router = APIRouter(prefix="/stories", tags=["Stories"])

@stories_router.get("/")
def get_story_router(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@stories_router.post("/")
def create_story(request: Request, topic = Form(None)):
    
    res = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": topic},
        ],
        extra_body={"reasoning": {"enabled": True}},
    )

    result = res.choices[0].message.content
    # return {"result": result}

    html = markdown.markdown(result)
    return template.TemplateResponse("story.html", {"request": request, "story": html})