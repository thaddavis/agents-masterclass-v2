# TLDR
Part 4 - Show how streaming increases the quality of UX

## 1 - Open the project in a `devcontainer`
- Shift + CMD + P
    - `Shell Command: Install 'code command in PATH`

## 2 - Run FastAPI server
- `uvicorn src.main:app --host 0.0.0.0 --port 4000 --reload`

## 3 - Show case the reference links outlining the technique of how this is done
- (Backend) https://github.com/thaddavis/agents-masterclass-v2/blob/05051d8342ec4d0abdd4b4510ae55b751950a537/lvl_9/src/_2_streamingAgent/router.py#L28
- (Frontend) https://github.com/thaddavis/agents-masterclass-v2-ui/blob/main/src/services/callStreamingAgent.ts
- Highlight the differences with Streaming and Completion Agents in LangSmith
    - time-to-first-token / Streaming percentage
    - tell the analogy of streaming media like audio & video
    - https://smith.langchain.com/o/2becc028-393d-5a8e-b0f6-23ba75a39a27/projects?paginationState=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A10%7D

### Reference Links
- https://www.vidavolta.io/streaming-with-fastapi/
- https://www.loginradius.com/blog/engineering/guest-post/http-streaming-with-nodejs-and-fetch-api/
- https://python.langchain.com/docs/expression_language/streaming/#using-stream-events
- https://docs.smith.langchain.com/tracing/faq/langchain_specific_guides#tracing-without-environment-variables