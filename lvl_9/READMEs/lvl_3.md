# TLDR
Phase 3

# Host Requirements
- A computer (`About This Mac` -> macOS Monterey 12.5 / Apple M1 Pro / 16 GB)
- Docker (`docker --version` -> 23.0.3)
- Visual Studio Code (`code -v` -> 1.87.2)
    - Node.js (lts/iron)
        - I'm using: 20.11.1
- gcloud CLI - 470.0.0
    - Python 3.11

## 1 - 

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
- add `Dockerfile5.dev`
- add `fastapi, uvicorn, & dotenv` to requirements.txt
- `uvicorn src.main:app --host 0.0.0.0 --port 4000 --reload`
- curl localhost:3000

## 3 - Prepare FastAPI file structure


### Reference material

- https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project#answer-64987404
- https://github.com/thaddavis/agents-masterclass/blob/main/api/src/main.py