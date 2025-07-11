#!/usr/bin/env python3
"""Module changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
   """Update the topics"""
   mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
