#!/usr/bin/env python3
"""Module inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Return ids"""
    return mongo_collection.insert_one(kwargs).inserted_id
