import time
from .redis_client import redis_client


class RateLimiter:
    LIMIT = 200
    WINDOW = 60

    @classmethod
    def allow_request(cls):
        key = "email_rate"
        count = redis_client.incr(key)

        if count == 1:
            redis_client.expire(key, cls.WINDOW)

        return count <= cls.LIMIT