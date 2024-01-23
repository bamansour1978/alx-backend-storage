#!/usr/bin/env python3
"""
Module Documentation-
"""
import pymongo


def list_all(mongo_collection):
    """
    Function Documentation
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())

