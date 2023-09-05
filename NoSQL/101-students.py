#!/usr/bin/env python3
"""
Task 14: returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Retrieves a list of top students based on their average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection containing student data.

    Returns:
        list: A list of dictionaries representing the top students, sorted by
        average score in descending order.
            Each dictionary contains the following keys:
                - "_id" (ObjectId): The unique identifier of the student
                document.
                - "name" (str): The name of the student.
                - "totalScore" (int): The total score of the student across
                all topics.
                - "topicCount" (int): The number of topics the student has
                scores for.
                - "averageScore" (float): The average score of the student
                across all topics.
    """
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "totalScore": {"$sum": "$topics.score"},
                "topicCount": {"$sum": 1}
            }
        },
        {
            "$addFields": {
                "averageScore": {"$divide": ["$totalScore", "$topicCount"]}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    result = list(mongo_collection.aggregate(pipeline))

    return result


if __name__ == "__main__":
    pass
