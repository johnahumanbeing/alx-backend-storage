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
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper
