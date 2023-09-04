#!/usr/bin/env python3
"""

"""
from pymongo import MongoClient


def log_stats():
    # Connect to the MongoDB database
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})

    # Get the count of each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in http_methods:
        count = collection.count_documents({"method": method})
        method_counts[method] = count

    # Get the count of logs with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
