#!/usr/bin/env python3
"""Module provides some stats about Nginx logs stored in MongoDB:"""
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
