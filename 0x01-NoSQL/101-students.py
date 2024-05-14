#!/usr/bin/env python3
""" agg operations: average
"""
from collections import OrderedDict


def top_students(mongo_collection):
    """
    Gets list of students from mongo collection
    & returns the list of computed average for
    each student
    """
    pipeline = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
                {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]
    return mongo_collection.aggregate(pipeline)
