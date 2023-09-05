#!/usr/bin/env python3
"""
Task 15: adding the top 10 of the most present IPs in the collection nginx of
the database logs.
"""
from pymongo import MongoClient


def log_stats():
    """
    Retrieves statistics from a MongoDB collection of nginx logs.

    Counts the total number of logs, the number of logs for each HTTP method,
    the number of logs with a specific path, and the top 10 most frequent IP
    addresses.

    Outputs:
    - The total number of logs.
    - The number of logs for each HTTP method.
    - The number of logs with a specific path.
    - The top 10 most frequent IP addresses and their counts.
    """

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count the number of documents in the collection
    total_logs = logs_collection.count_documents({})

    print(f"{total_logs} logs")

    print("Methods:")
    # Count the number of documents with each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of documents with status check
    status_check_count = logs_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

    # Count the top 10 most present IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    ip_counts = logs_collection.aggregate(pipeline)

    print("IPs:")
    for ip_count in ip_counts:
        ip = ip_count["_id"]
        count = ip_count["count"]
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    log_stats()
