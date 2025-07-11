#!/usr/bin/env python3
"""Module lists all documents in the collection"


def list_all(mongo_collection):
    """Return the list of documents"""
    return list(mongo_collection.find())
