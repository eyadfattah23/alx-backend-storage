#!/usr/bin/env python3
"""
Define a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """lists all documents in a collection

        Args:
            mongo_collection (pymongo collection object)
        """

    documents = mongo_collection.find()
    return [doc for doc in documents]
