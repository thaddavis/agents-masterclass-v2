# TLDR
Part 3

# Host Requirements
- A computer (`About This Mac` -> macOS Monterey 12.5 / Apple M1 Pro / 16 GB)
- Docker (`docker --version` -> 23.0.3)
- Visual Studio Code (`code -v` -> 1.87.2)
    - Node.js (lts/iron)
        - I'm using: 20.11.1
- gcloud CLI - 470.0.0
    - Python 3.11

## 1 - Open the project in a `devcontainer`
- Shift + CMD + P
    - `Shell Command: Install 'code command in PATH`

## 2 - Let's begin building the FastAPI
- update `src/main.py`
```
from fastapi import FastAPI
import debugpy

debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```
- add `Dockerfile.dev`
- add `fastapi, uvicorn, & python-dotenv` to requirements.txt
- `uvicorn src.main:app --host 0.0.0.0 --port 4000 --reload`
- curl localhost:3000

## 3 - Prepare FastAPI file structure
- scaffold out the 5 agent we will be building
    - `Completion Agent`
    - `Streaming Agent`
    - `RAG Agent`
    - `Plan & Execute Agent`
    - `Agent Swarm`

## 4 - Integrate and LLM API via Langchain
- You could use LLM provided by OpenAI, Google, or Anthropic etc.
- To mix things up let's give `claude-3-sonnet-20240229` a spin, an LLM provided by Anthropic.
- add `langchain-anthropic` to requirements.txt
- pip install -r requirements.txt

## 5 - Integrate LangSmith
- Add the env vars for LangSmith
- Observe the `traces` and point out the following details...
    - Latency
    - So... let's test with a slightly larger prompt ie:
        - maybe you want to have an LLM read a book for you and generate customized cliff notes
        - or maybe you want an LLM to help you negotiate a contract
        - etc.
    - use your imagination but for demonstration purposes let's have "Claude" summarize the 9 pages of the paper that outlined the design of the Bitcoin protocol
    - I've noticed that the more text you send with your prompts the longer it tends to take LLM's to return their complete responses
    - And you can see in LangSmith that this seems to be true
    - So now let's look at a trick for how to make transformers respond to you MUCH faster


### Reference material
- https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project#answer-64987404
- https://github.com/thaddavis/agents-masterclass/blob/main/api/src/main.py
- https://www.langchain.com/langsmith