#!/usr/bin/env python3
"""Define a Cache class."""

import redis
import uuid
from typing import Union, Callable, Awaitable, Any


class Cache:
    """Redis Cache class.
    """

    def __init__(self):
        """initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """set a new key/value pair in the cache

        Args:
            data (any): data to be stored in the cache.

        Returns:
            str: uuid key of the new data stored in the cache.
        """
        new_key = str(uuid.uuid4())
        self._redis.set(new_key, data)
        return new_key

    def get(self, key: str, fn: Callable = None) ->\
            Union[Awaitable, Any, None]:
        """get a key/value pair in the cache


        Args:
            key (str): key of the piece of data to retrieve
            fn (Callable, optional): convert data back to the desired format.
                                    Defaults to None.
        """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, key: str, fn: Callable = None) ->\
            Union[Awaitable, Any, None]:
        """get a key/value pair in the cache


        Args:
            key (str): key of the piece of data to retrieve
            fn (Callable, optional): convert data back to the desired format.
                                    Defaults to None.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str, fn: Callable = None) ->\
            Union[Awaitable, Any, None]:
        """get a key/value pair in the cache


        Args:
            key (str): key of the piece of data to retrieve
            fn (Callable, optional): convert data back to the desired format.
                                    Defaults to None.
        """
        return self.get(key, int)


""" Test Block 0
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}


for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
"""
