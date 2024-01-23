#!/usr/bin/env python3
"""
Module Documentation 
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Function Documentattion
    """
    return mongo_collection.find({"topics": topic})

