# Project: 0x02. Redis basic

## Resources

#### Read or watch:

* [Redis Crash Course Tutorial]
* [Redis commands]
* [Redis python client]
* [How to Use Redis With Python]
'

## Tasks
0. Writing string to Redis:
    - class `Cache` implementation
    - method `store` implementation
    - File: [exercise.py](exercise.py)

1. Reading from Redis and recovering original type using `redis-py`
    - Methods implementation: `get_str` and `get_int`
    - File: [exercise.py](exercise.py)

2. Incrementing values on Redis
    - Implementation of `count calls` function-based decorator for `Cache.store`  method
    - File: [exercise.py](exercise.py)

3. Storing list elements in Redis
    - Implementation of `call_history` function-based decorator for `Cache.store` method.
    - File: [exercise.py](exercise.py)

4. Retrieving list elements from Redis
    - Implementation of `replay` function to display history of a particular function based on data retrieved from Redis
    - File: [exercise.py](exercise.py)

5. Implementing an expiring web cache and tracker
    - Function `get_page` for making requests and tracking url access count
    - File: [web.py](web.py)
