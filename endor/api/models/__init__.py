from sqlalchemy import create_engine, MetaData, event
from sqlalchemy.orm import scoped_session, sessionmaker, object_session, mapper
from sqlalchemy.ext.declarative import declarative_base

class _EntityBase(object):
    """
    A custom declarative base that provides some Elixir-inspired shortcuts.
    """

    @classmethod
    def filter_by(cls, *args, **kwargs):
        return cls.query.filter_by(*args, **kwargs)

    @classmethod
    def get(cls, *args, **kwargs):
        return cls.query.get(*args, **kwargs)

    def flush(self, *args, **kwargs):
        object_session(self).flush([self], *args, **kwargs)

    def delete(self, *args, **kwargs):
        object_session(self).delete(self, *args, **kwargs)

    def as_dict(self):
        return dict((k, v) for k, v in self.__dict__.items()
                    if not k.startswith('_'))

Session = scoped_session(sessionmaker())
metadata = MetaData()
Base = declarative_base(cls=_EntityBase)
Base.query = Session.query_property()


# Listeners:
@event.listens_for(mapper, 'init')
def auto_add(target, args, kwargs):
    Session.add(target)


def init_model(conf):
    """
    This is a stub method which is called at application startup time.
    If you need to bind to a parse database configuration, set up tables or
    ORM classes, or perform any database initialization, this is the
    recommended place to do it.
    For more information working with databases, and some common recipes,
    see http://pecan.readthedocs.org/en/latest/databases.html
    For creating all metadata you would use::
        Base.metadata.create_all(conf.sqlalchemy.engine)
    """

    engine=_engine_from_config(conf)
    Session.configure(bind=engine)
    return Session


def _engine_from_config(configuration):
    configuration=dict(configuration)
    url=configuration.pop('url')
    engine=create_engine(url, **configuration)
    return engine


def start(conf):
    Session()
    metadata.bind = _engine_from_config(conf) # conf.sqlalchemy.engine


def start_read_only(conf):
    start(conf)


def commit():
    Session.commit()


def rollback():
    Session.rollback()


def clear():
    Session.remove()
    Session.close()


def flush():
    Session.flush()

from assigment import Assigment
from condition import Condition
from country import Country
from customer_project import CustomerProject
from customer import Customer
from devolution import Devolutions
from employee import Employee
from fee import Fee
from group import Group
from position import Position
from postal_address import PostalAddress
from role import Role
from schedule_window import ScheduleWindow
from schedule import Schedule
from ubiego import Ubigeo
from user import User
from weekday import Weekday
