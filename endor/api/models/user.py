from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class User(Base):
    __tablename__ = "users"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(UUIDType(binary=False), unique=True, nullable=False)
    enabled = Column(Boolean, default=True)

    # Roles for User
    role_id = Column(UUIDType(binary=False), ForeignKey('roles.id'))
    role = relationship("Role", back_populates="user")

    # Employee for User
    employee_id = Column(UUIDType(binary=False), ForeignKey('employees.id'))
    employee = relationship("Employee", back_populates="user")

    def __repr__(self):
        return '<User {}|{}>'.format(self.id, self.username)

    def __json__(self):
        return dict(
            id=self.token,
            username=self.username,
            password=self.password,
            token=self.token,
            enabled=self.enabled,
        )
