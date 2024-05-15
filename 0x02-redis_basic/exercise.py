#!/usr/bin/env python3
""" Redis exercise
"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """ Count the number of times a method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Store the history of inputs and outputs for a method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function
        """
        input = str(args)
        self._redis.rpush(f"{method.__qualname__}:inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(f"{method.__qualname__}:outputs", output)

        return output
    return wrapper
