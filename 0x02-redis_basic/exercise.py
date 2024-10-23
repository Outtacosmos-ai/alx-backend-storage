#!/usr/bin/env python3
"""
Redis basic exercise
"""
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class to interact with Redis """

    def __init__(self):
        """ Initialize Redis connection and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key and return the key
        :param data: str, bytes, int or float
        :return: the generated key (str)
        """
        key = str(uuid.uuid4())  # Generate a random key
        self._redis.set(key, data)  # Store the data in Redis
        return key
