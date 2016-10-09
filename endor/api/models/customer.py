from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Customer(Base):
    __tablename__ = "customers"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)

    # Relation for postal_address
    postal_address = relationship(
                                  "PostalAddress",
                                  order_by="postal_address.id",
                                  back_populates="customer")

    # Relation for Cutomer Projects
    cutomer_project = relationship(
                                  "CustomerProject",
                                  order_by="customer_projects.id",
                                  back_populates="customer")

    def __repr__(self):
        return '<Customer {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
        )
