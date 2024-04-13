from fastapi import APIRouter
from langchain_anthropic import ChatAnthropic
from pydantic import BaseModel
from core.schemas.Prompt import Prompt

from fastapi.responses import StreamingResponse

router = APIRouter()

async def generator():
    model: str = "claude-3-sonnet-20240229"
    llm = ChatAnthropic(model=model, temperature=0.2, max_tokens=1024)
    for chunk in llm.stream("Write me a song about goldfish on the moon"):
        yield chunk.content

@router.post("/completion")
def prompt(prompt: Prompt):
    

    # chat = ChatAnthropic(model="claude-2")
    # for chunk in chat.stream("Write me a song about goldfish on the moon"):
    #     print(chunk.content, end="", flush=True)

    return StreamingResponse(generator(), media_type='text/event-stream')

    # return {"completion": completion.content}

    # completion = llm.invoke(prompt.content)
    # return {"completion": completion.content}