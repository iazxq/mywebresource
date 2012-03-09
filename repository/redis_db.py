# -*- coding: utf-8 -*-

import redis

class RedisDB:
    def __init__(self):
        self.redis = redis.Redis()


    def dispose(self):
        pass


    def __enter__(self):
        return self

    def  __exit__(self, type, value, traceback):
        self.dispose()