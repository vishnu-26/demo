import redis

def redis_connect():
    r = redis.StrictRedis(
        host='redis-app',
        port= 6379,
        charset="utf-8",
        decode_responses=True
        )

    print("Connected to Redis!!")
    return r
