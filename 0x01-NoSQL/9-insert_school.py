#!/usr/bin/env python3
"""
Define a Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs

        Args:
            mongo_collection (pymongo collection object)
            kwargs (dict): data to insert into the collection
        """

    return mongo_collection.insert_one(kwargs).inserted_id