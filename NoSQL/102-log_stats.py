#!/usr/bin/env python3
"""Module provides some stats about Nginx logs stored in MongoDB and
adds the top 10 of the most present IPs in the collection nginx
 of the database logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs\nMethods:")

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for element in method:
        count = collection.count_documents({"method": element})
        print(f"\tmethod {element}: {count}")
    check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{check} status check")
    pipeline = [
        {"$group": {
                "_id": "$ip",
                "count": {"$sum": 1}}
        },

        {"$sort": {"count": -1}
        },

        {"$limit": 10}
    ]
    result = list(collection.aggregate(pipeline))
    print(f"IPs:")
    for i in range(len(result)):
        print(f"\t{result[i]['_id']}: {result[i]['count']}")
