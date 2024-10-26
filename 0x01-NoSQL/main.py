#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    sale_collection = client.test.sales
    sales = list_all(sale_collection)
    for sale in sales:
        print("[{}] {}".format(sale.get('_id'), sale.get('item')))
