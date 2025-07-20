#!/usr/bin/env python3
"""Module sorts students by their average scores"""


def top_students(mongo_collection):
    """Return all students sorted by average"""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
