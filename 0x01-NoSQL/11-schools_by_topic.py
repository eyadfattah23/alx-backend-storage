#!/usr/bin/env python3
"""
Define function that changes all topics of a school document based on the name
"""


def schools_by_topic(mongo_collection, topic):
    """changes all topics of a school document based on the name

    Args:
        mongo_collection (pymongo collection object)
        topic (string): school name to update

    Returns:
        None
    """

    return [school for school in mongo_collection.find({"topics": {"$in": [topic]}})]
