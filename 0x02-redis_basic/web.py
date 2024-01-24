#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from datetime import timedelta


def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    if not url or not url.strip():
        return ''

    redis_store = redis.Redis()
    res_key = f'result:{url}'
    req_key = f'count:{url}'

    try:
        result = redis_store.get(res_key)
        if result is not None:
            redis_store.incr(req_key)
            return result.decode('utf-8')

        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.content.decode('utf-8')

        redis_store.setex(res_key, timedelta(seconds=10), result)
        redis_store.incr(req_key)
        return result

    except requests.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return ''
