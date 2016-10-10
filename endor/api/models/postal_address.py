from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class PostalAddress(Base):
    __tablename__ = "postal_addresses"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    house_number = Column(String, nullable=False)
    street_name = Column(String, nullable=False)

    # Country for PostalAddress
    country_id = Column(String, ForeignKey('countries.id'))
    country = relationship("Country", back_populates="postal_address")

    # Ubigeo for PostalAddress
    ubigeo_id = Column(String, ForeignKey('ubigeos.id'))
    ubigeo = relationship("Ubigeo", back_populates="postal_address")

    # Customer for PostalAddress
    customer_id = Column(UUIDType(binary=False), ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="postal_address")


    def __repr__(self):
        return '<PostalAddress {}|{}>'.format(self.id, self.customer)

    def __json__(self):
        return dict(
            id=self.id,
            house_number=self.house_number,
            street_name=self.street_name,
            country=self.country,
            ubigeo=self.ubigeo,
            customer=self.customer,
        )
