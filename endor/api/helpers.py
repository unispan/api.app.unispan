# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from urlparse import parse_qs


def map_query(string):

    query_map = parse_qs(string)
    if not query_map:
        return query_map

    for k, v in query_map.iteritems():
        if len(v) == 1:
            # 'unlist' values when they are a list of 1 item
            query_map[k] = v[0]

    return query_map


def json_default(obj):

    if isinstance(obj, timedelta):
        return {"$timedelta": float(obj.total_seconds())}
    if isinstance(obj, datetime):
        return {"$date": datetime.strftime(obj, "%Y-%m-%dT%H:%M:%S.%fZ")}
    raise TypeError("%r is not JSON serializable" % obj)
