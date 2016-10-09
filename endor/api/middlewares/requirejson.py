# -*- coding: utf-8 -*-
import falcon
from endor.api.exception import HTTPError

class RequireJSON(object):

    def process_request(self, req, resp):
        if not req.client_accepts_json and not req.client_accepts_xml:
            raise HTTPError(facon.HTTP_406,
                "This API only supports responses encoded as JSON or XML",
                "This API only supports responses encoded as JSON or XML")
        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.',
                    href='http://docs.examples.com/api/json')
