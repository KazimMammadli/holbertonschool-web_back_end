#!/usr/bin/env python3
"""Module returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools with specified topic"""
    return list(mongo_collection.find({"topics": topic}))
