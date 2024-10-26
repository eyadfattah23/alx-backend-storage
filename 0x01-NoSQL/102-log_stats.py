#!/usr/bin/env python3
"""
Define a script that provides some stats about Nginx logs stored in MongoDB:

* Database: logs
* Collection: nginx
* Display (same as the example):
* * first line: x logs where x is the number of documents in this collection
* * second line: Methods:
* * 5 lines with the number of documents with the method =
                ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
* * one line with the number of documents with:
* * * method=GET
* * * path=/status

"""
from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs_collection = client.logs.nginx

    print("{} logs".format(nginx_logs_collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(
        nginx_logs_collection.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(
        nginx_logs_collection.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(
        nginx_logs_collection.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(
        nginx_logs_collection.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(
        nginx_logs_collection.count_documents({"method": "DELETE"})))

    print("{} status check".format(
        nginx_logs_collection.count_documents({"path": "/status"})))
    print("IPs:")

    query = nginx_logs_collection.aggregate(
        [
            {

                "$group": {
                    "_id": "$ip",
                    "ip_count": {"$sum": 1}
                },


            },
            {"$sort": {"ip_count": -1}},
            {"$limit": 10}
        ]
    )

    for ip_stats in query:
        print("\t{}: {}".format(ip_stats.get('_id'), ip_stats.get('ip_count')))
