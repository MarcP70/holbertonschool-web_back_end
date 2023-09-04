#!/usr/bin/env python3
"""
Task 10: changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a school document based on the school's name.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo
            collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics to replace the existing
            topics.

    Returns:
        None
    """
    # Define the filter to find the school by name
    filter = {"name": name}

    # Define the update operation to set the new topics
    update = {"$set": {"topics": topics}}

    # Use the update_one method to update the document
    mongo_collection.update_one(filter, update)


if __name__ == "__main__":
    pass
