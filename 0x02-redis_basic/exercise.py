#!/usr/bin/env python3
"""A redis exercise module"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """A cache class"""

    def __init__(self):
        """initialize a cavhe instance and redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store a data in redis using a unique identifier"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
