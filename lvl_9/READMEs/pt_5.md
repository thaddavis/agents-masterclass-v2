# TLDR
Part 5 - Including Memory

## 1 - Run redis

- docker network create -d bridge agent-network
- docker network ls
- docker run --network agent-network --name agent-memory -p 6739:6739 -d redis
- docker network connect agent-network 21b16700305fbca55d8a4d2d935daffd83505c885344f07ebad09e231d5cb8d4 <!-- ie: the devcontainer -->

- docker inspect --format='{{json .NetworkSettings.Networks}}' agent-memory | jq
- docker inspect --format='{{json .NetworkSettings.Networks}}' 21b16700305fbca55d8a4d2d935daffd83505c885344f07ebad09e231d5cb8d4 | jq


## 2 - Build redis integration

- Add .env var for connecting to Redis
- Populate `_3_streamingWithMemoryAgent/router.py` with code
- add the following pip packages
    - redis
    - 

## Reference links

- https://python.langchain.com/docs/use_cases/tool_use/agents/
- https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/
- https://python.langchain.com/docs/modules/model_io/prompts/quick_start/