# -*- coding: utf-8 -*-
import os
import sys
import click
import falcon

from endor.config import get_config
from endor.api import models
from endor.api.middlewares.cors import CORSMiddleware
from endor.api.middlewares.requirejson import RequireJSON
from endor.api.controllers.roles import RoleColletions
from endor.api.controllers.roles import RoleResource
from endor.api.exception import HTTPError


from endor import __version_api__


class App(object):
    """App for api Unispan."""

    def __init__(self, context):
        """Initialize APP for api Unispan."""
        self.context = context
        self.db_section = self._get_db_section()
        self.db_name = None

        # add middlewares
        self.api = falcon.API(middleware=[
            CORSMiddleware(self.context.config['middleware']['cors']),
            RequireJSON()
        ])

        # get Backing Services from config file
        self._get_config_backing_services()

        # setup database
        # self._setup_db()

        # load routes
        self._load_routes()

    def _load_routes(self):
        uri_base = '/api/v{}'.format(__version_api__)
        routes = [
            # Roles
            ("%s/roles" % uri_base, RoleColletions(self.context)),
            ("%s/roles/{company_id}" % uri_base, RoleResource(self.context))

        ]

        for (uri_template, resource) in routes:
            self.api.add_route(uri_template, resource)

    def _get_db_section(self):
        return get_config()['DB_SECTION']

    def _get_config_backing_services(self):
            self.context.backingServices = \
                self.context.config['backingServices'][self.db_section]

    def _setup_db(self):
        try:
            self.db_name = models.init_model(
                self.context.backingServices
            )
        except:
            user_message = 'No exists Configurations for {}' \
                                .format(self.db_section)
            developer_message = user_message
            raise HTTPError(406, developer_message, user_message)
        self.context.log('connected to Database: {}'.format(self.db_name))
