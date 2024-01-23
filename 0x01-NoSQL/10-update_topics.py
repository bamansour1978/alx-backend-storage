#!/usr/bin/env python3
"""
Module Documentation
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Function Documentation
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

