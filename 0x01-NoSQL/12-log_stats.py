#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx
"""
from pymongo import MongoClient


def print_nginx_logs_stats():
    """
    Function that provides stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    print_nginx_logs_stats()
