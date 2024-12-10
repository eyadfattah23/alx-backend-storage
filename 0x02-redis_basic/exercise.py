#!/usr/bin/env python3
"""Define a Cache class."""

import redis
import uuid
from typing import Union, Callable, Awaitable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """#+
    Decorator function to count the number of times a method is called.#+
#+
    this decorator is used to incr. a counter in Redis for each call to method
    The counter key is the fully qualified name of the method.#+
#+
    Args:#+
        method (Callable): The method to be decorated.#+
#+
    Returns:#+
        Callable: The decorated method.#+
    """  # +
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """#+
    Decorator to record the call history of a method.#+
#+
    This decorator logs the inputs and outputs of each method call in Redis.#+
    It creates two lists in Redis:#+
    - One for inputs, with key "{method_name}:inputs"#+
    - One for outputs, with key "{method_name}:outputs"#+
#+
    Args:#+
        method (Callable): The method to be decorated.#+
#+
    Returns:#+
        Callable: The decorated method that logs its calls.#+
    """  # +
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method_name = method.__qualname__
        output = method(self, *args, **kwargs)
        self._redis.rpush("{}:inputs".format(method_name), str(args))
        self._redis.rpush("{}:outputs".format(method_name), str(output))
        return output

    return wrapper


def replay(method: Callable) -> Callable:
    """#+
    Replay and display the call history of a method.#+
#+
    This function retrieves and displays the call history of a given method#+
    from Redis, including the number of times it was called and the#+
    inputs and outputs for each call.#+
#+
    Args:#+
        method (Callable): The method whose call history is to be replayed.#+
#+
    Returns:#+
        Callable: The original method, unchanged.#+
#+
    Note:#+
        This function assumes that the method's call history has been#+
        previously recorded in Redis using the @call_history decorator.#+
    """  # +
    method_name = method.__qualname__
    _redis = redis.Redis()
    number_calls = _redis.get(method_name).decode("utf-8")
    print("{} was called {} times:".format(method_name, number_calls))
    inputs = _redis.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = _redis.lrange("{}:outputs".format(method_name), 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """Redis Cache class.
    """

    def __init__(self):
        """initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

"""
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
"""
