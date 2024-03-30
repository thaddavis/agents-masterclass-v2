from fastapi import FastAPI
import redis

import debugpy

debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()

r = redis.Redis(host="redis", port=6379)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}