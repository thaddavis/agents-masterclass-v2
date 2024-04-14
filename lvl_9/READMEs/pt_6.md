# TLDR
Part 6 - R.A.G. Agents (w/ Chroma and OpenAI)

## Install & Run ChromaDB

- apt-get install build-essential
- pip install chromadb
- git clone https://github.com/chroma-core/chroma
    - cd chroma

- docker build -f Dockerfile -t chromadb .
- docker run --network agent-network --name chromadb -p 9000:9000 -d chromadb
    - make sure `agent-network` is created ie: `docker network create -d bridge agent-network`
- docker inspect --format='{{json .NetworkSettings.Networks}}' chromadb | jq

## Play with ChromaDB

- python scripts/chromadb/playground.py

## Content sequence is...

1. Explain how R.A.G. agents require a preparation step to work
    - https://python.langchain.com/docs/modules/data_connection/vectorstores (great photo)
1. The Vector DB we will be using is called `Chroma`
    - Scan the ChromaDB docs
1. Create a collection and add the 'knowledge base' that we will seed our R.A.G. agent with...
    - scan the knowledge base
    - run the `scripts/chromadb/add_csv_records.py` script
    - test a query 'Tell me about Tad Duval'
1. Previous step with explicit commands...
    - `python scripts/chromadb/create_collection.py`
    - `python scripts/chromadb/count_records_in_collection.py`
    - `python scripts/chromadb/add_csv_records.py `
1. Now! We build out the application

## Reference links
- https://python.langchain.com/docs/modules/data_connection/vectorstores/ (great photo)
- https://docs.trychroma.com/getting-started
- https://github.com/chroma-core/chroma/blob/main/docker-compose.yml
- http://onnx.ai/models/
- https://www.sbert.net/