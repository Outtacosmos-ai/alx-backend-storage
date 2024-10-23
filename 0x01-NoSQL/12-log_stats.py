#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def print_nginx_logs_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    print_nginx_logs_stats()
