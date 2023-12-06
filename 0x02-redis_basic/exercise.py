#!/usr/bin/env python3
"""A redis exercise module"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """Counts how many times a method is called"""
    @wraps(fn)
    def wrapper(self, arg):
        """wrapper func"""
        key = fn.__qualname__
        if not self._redis.exists(key):
            self._redis.set(key, 0)
        self._redis.incr(key)
        return fn(self, arg)
    return wrapper


class Cache:
    """A cache class"""

    def __init__(self):
        """initialize a cavhe instance and redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store a data in redis using a unique identifier"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """Get the data from redis"""
        data = self._redis.get(key)
        if data and fn:
            return fn(data)
        return data

    def get_str(self, data):
        """convert to a string"""
        return str(data)

    def get_int(self, data):
        """convert to an integer"""
        return int(data)
