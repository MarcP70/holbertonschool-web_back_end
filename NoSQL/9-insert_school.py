#!/usr/bin/env pyton3
"""
Task 9: inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection based on keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo
            collection object.
        **kwargs: Keyword arguments representing the document fields and
            values.

    Returns:
        str: The new document's _id.
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return str(result.inserted_id)


if __name__ == "__main__":
    pass
