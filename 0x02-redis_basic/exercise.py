#!/usr/bin/env python3
"""Define a Cache class."""

import redis
import uuid


class Cache:
    """Redis Cache class.
    """

    def __init__(self):
        """initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """set a new key/value pair in the cache

        Args:
            data (any): data to be stored in the cache.

        Returns:
            str: uuid key of the new data stored in the cache.
        """
        new_key = str(uuid.uuid4())
        self._redis.set(new_key, data)
        return new_key
