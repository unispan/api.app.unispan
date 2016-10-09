from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Group(Base):
    __tablename__ = "groups"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for Equipment
    equipment = relationship(
                            "Equipment",
                            order_by="equipments.id",
                            back_populates="group")

    # Relation for Fee
    fee = relationship(
                        "Fee",
                        order_by="fees.id",
                        back_populates="group")

    def __repr__(self):
        return '<Group {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            name=self.name,
            enabled=self.enabled,
        )
