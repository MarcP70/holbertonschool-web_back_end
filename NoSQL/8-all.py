#!/usr/bin/env python3
"""
Task 8: List all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo
        collection object.

    Returns:
        list: A list of documents in the collection.
    """
    documents = list(mongo_collection.find())
    return documents


if __name__ == "__main__":
    pass
