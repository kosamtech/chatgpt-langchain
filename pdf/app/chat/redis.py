import os
import redis

client = redis.Redis.from_url(os.environ.get("REDIS_URI"),decode_responses=True)

