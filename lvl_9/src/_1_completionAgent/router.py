from fastapi import APIRouter
from langchain_anthropic import ChatAnthropic
from pydantic import BaseModel
from core.schemas.Prompt import Prompt

router = APIRouter()

class ResponseBody(BaseModel):
    completion: str

@router.post("/completion")
def prompt(prompt: Prompt) -> ResponseBody:
    llm = ChatAnthropic(
        model="claude-3-sonnet-20240229", temperature=0.2, max_tokens=1024
    )

    completion = llm.invoke(prompt.content)

    return {"completion": completion.content}