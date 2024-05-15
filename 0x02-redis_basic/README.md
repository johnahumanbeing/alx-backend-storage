# Project: 0x02. Redis basic

## Resources

#### Read or watch:

* [Redis Crash Course Tutorial]
* [Redis commands]
* [Redis python client]
* [How to Use Redis With Python]
## Learning Objectives

### General

* All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All of your files should end with a new line
* A <code>README.md</code> file, at the root of the folder of the project, is mandatory
* The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
* Your code should use the <code>pycodestyle</code> style (version 2.5)
* All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
* All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)
* All your functions and methods should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.

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

## Tasks

| Task | File |
| ---- | ---- |
| 0. Writing strings to Redis | [exercise.py](./exercise.py) |
| 1. Reading from Redis and recovering original type | [exercise.py](./exercise.py) |
| 2. Incrementing values | [exercise.py](./exercise.py) |
| 3. Storing lists | [exercise.py](./exercise.py) |
| 4. Retrieving lists | [exercise.py](./exercise.py) |
| 5. Implementing an expiring web cache and tracker | [web.py](./web.py) |