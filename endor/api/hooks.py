# -*- coding: utf-8 -*-

from __future__ import absolute_import
from endor.api.helpers import map_query
from falcon import HTTPBadRequest, HTTPNotAcceptable
import json
import colander


def deserialize(req, rep, resource, params, schema=None):
    """Deserializes data from the request object based on HTTP method.

    A BEFORE hook function

    Deserializes data from the request object based on HTTP method
    if a colander Schema is provided, further deserialize data with the schema
    updates req.params with the deserialized data, in either 'body' or 'query'
    key
    :param req: request object
    :param res: response object
    :param resource: response pbject
    :param schema: colander Schema object
    """

    def _is_json_type(content_type):
        return content_type == 'application/json'

    if req.method.upper() in ['POST', 'PUT', 'DELETE']:

        if not _is_json_type(req.content_type):
            raise HTTPNotAcceptable(description='JSON required. '
                                    'Invalid Content-Type\n{}'
                                    .format(req.content_type))

        req.params['body'] = {}

        stream = req.stream.read()
        if not stream:
            return

        if schema:
            try:
                json_body = json.loads(stream)
                body = schema.deserialize(json_body)

            except ValueError as e:
                raise HTTPBadRequest(title='Invalid json',
                                     description='Invalid arguments '
                                                 'in params:\n{}'
                                                 .format(e.message))
            except colander.Invalid as e:
                raise HTTPBadRequest(title='Invalid Value',
                                     description='Invalid arguments '
                                                 'in params:\n{}'
                                                 .format(e.asdict()))

        req.params['body'] = body

    elif req.method.upper() == 'GET':

        req.params['query'] = {}

        if not req.query_string:
            return

        query = map_query(req.query_string)

        if schema:
            try:
                query = schema.deserialize(query)
            except colander.Invalid as e:
                raise HTTPBadRequest(title='Invalid Value',
                                     description='Invalid arguments '
                                                 'in params:\n{}'
                                                 .format(e.asdict()))

        req.params['query'] = query


def serialize(req, res, resource, params):
    """
    An AFTER hook function.

    Serializes the data from dict to json-formatted string
    :param req: request object
    :param res: response object
    :param resource: resource object
    """
    def _to_json(obj):
        # base cases:
        if isinstance(obj, dict):
            return {k: _to_json(v) for k, v in obj.iteritems()}
        return obj

    res.body = json.dumps(_to_json(res.body))
