#!/usr/bin/env python3
"""
Task 11: Retrieve a list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo
            collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents matching the specified topic.
    """
    # Define the filter to find schools with the specified topic
    filter = {"topics": topic}

    # Use the find method to retrieve matching documents
    schools = list(mongo_collection.find(filter))

    return schools


if __name__ == "__main__":
    pass
