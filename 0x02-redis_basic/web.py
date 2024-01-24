#!/usr/bin/env python3
"""
Module documentation
"""
import redis
import requests
from datetime import timedelta


def get_page(url: str) -> str:
    """
    Function documentation
    """
    if url is None or len(url.strip()) == 0:
        return ""
    redis_store = redis.Redis()
    res_key = 'result:{}'.format(url)
    req_key = 'count:{}'.format(url)
    reslt = redis_store.get(res_key)
    if reslt is not None:
        redis_store.incr(req_key)
        return reslt
    reslt = requests.get(url).content.decode('utf-8')
    redis_store.setex(res_key, timedelta(seconds=10), reslt)
    return reslt
