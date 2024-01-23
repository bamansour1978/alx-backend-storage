#!/usr/bin/env python3
"""
Module Documentation
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Function Documentation
    """
    return mongo_collection.insert_one(kwargs).inserted_id

