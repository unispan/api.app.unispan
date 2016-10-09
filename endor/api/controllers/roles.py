# -*- coding: utf-8 -*-
import falcon
import json
import logging

from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError, StatementError
from sqlalchemy.orm.exc import NoResultFound

from endor.api import models
from endor.api import schemas

from endor.api.hooks import deserialize, serialize
from endor.api.exception import HTTPError
from endor.config import get_config


logger = logging.getLogger(__name__)


def deserialize_create(req, res, resource, params):
    """Deserialize role schema."""
    logger.info('Deserialize create Role')
    deserialize(req, res, resource, params, schema=schemas.Role())


class RoleColletions(object):
    """."""

    def __init__(self, context):
        """Initialize the role collections."""
        self.context = context

    @falcon.before(serialize)
    def on_get(self, req, resp):
        """Get All Roles."""
        try:
            roles = models.Role.query.all()
            resp.body = json.dumps(roles, indent=4)
        except (NoResultFound, StatementError), e:
            raise HTTPError(falcon.HTTP_404, e.message, e.message)

    @falcon.before(deserialize_create)
    def on_post(self, req, resp):
        """."""
        try:
            role = req.get_param("body")
            role.update({
                'enabled': True
            })

        except SQLAlchemyError as e:
            raise HTTPError(falcon.HTTP_500, e.message, e.message)


class RoleResource(object):
    """."""

    def __init__(self, context):
        """Initialize the role resource."""
        self.context = context

    @falcon.before(serialize)
    def on_get(self, req, resp, role_id):
        """."""
        try:
            role = {}
            resp.body = json.dumps(role, indent=4)
        except (NoResultFound, StatementError), e:
            raise HTTPError(falcon.HTTP_404, e.message, e.message)

    def on_delete(self, req, resp, role_id):
        """."""
        try:

            resp.status = falcon.HTTP_NO_CONTENT
        except (NoResultFound, StatementError) as e:
            raise HTTPError(falcon.HTTP_404, e.message, e.message)

    @falcon.before(deserialize_create)
    def on_put(self, req, resp, role_id):
        """."""
        try:
            role = req.get_param("body")
        except SQLAlchemyError, e:
            raise HTTPError(falcon.HTTP_500, e.message, e.message)
