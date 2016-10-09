# -*- coding: utf-8 -*-

class CORSMiddleware(object):

    def __init__(self, config):
        self.config = config

    def process_request(self, req, resp):
        allowed_origins = self.config['allowed_origins'].split(',')
        allowed_headers = self.config['allowed_headers']
        # allowed_methods = self.config['allowed_methods']
        origin = req.get_header('Origin')
        header = {
            'Access-Control-Allow-Headers': allowed_headers
            # 'Access-Control-Allow-Methods': allowed_methods
        }
        if origin in allowed_origins:
            header['Access-Control-Allow-Origin'] = origin
        header['Access-Control-Allow-Origin'] = '*'
        resp.set_headers(header)
