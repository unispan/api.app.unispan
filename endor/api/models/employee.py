from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Employee(Base):
    __tablename__ = "employees"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    status = Column(Boolean, default=True)

    # Possiton for Employee
    position_id = Column(UUIDType(binary=False), ForeignKey('positions.id'))
    position = relationship("Position", back_populates="employee")

    # Relation for User
    user = relationship(
                    "User",
                    order_by="users.id",
                    back_populates="employee")

    # Relation for Customer Project
    customer_project = relationship(
                    "CustomerProject",
                    order_by="customer_projects.id",
                    back_populates="employee")

    def __repr__(self):
        return '<Employee {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            position=self.position,
            status=self.status,
        )
