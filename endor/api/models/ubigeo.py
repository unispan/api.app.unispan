from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Ubigeo(Base):
    __tablename__ = "ubigeos"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    department = Column(String, nullable=False)
    province = Column(String, nullable=False)
    district = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for Postal Address
    postal_address = relationship(
                                  "Ubigeo",
                                  order_by="ubigeos.id",
                                  back_populates="ubigeo")

    # Relation for Customer Projects
    customer_project = relationship(
                                  "CustomerProject",
                                  order_by="customer_projects.id",
                                  back_populates="ubigeo")

    def __repr__(self):
        return '<Ubigeo {}|{}|{}|{}|>'.format(
                                    self.id,
                                    self.department,
                                    self.province,
                                    self.district,
                                    )

    def __json__(self):
        return dict(
            id=self.id,
            department=self.department,
            province=self.province,
            district=self.district,
            enabled=self.enabled,
        )
