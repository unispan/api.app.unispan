from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Country(Base):
    __tablename__ = "countries"
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for Postal Address
    postal_address = relationship(
                                  "PostalAddress",
                                  order_by="postal_addresses.id",
                                  back_populates="country")

    # Relation for Customer Project
    customer_project = relationship(
                                    "Country",
                                    order_by="customer_projects.id",
                                    back_populates="country")

    def __repr__(self):
        return '<Country {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            enabled=self.enabled,
        )
