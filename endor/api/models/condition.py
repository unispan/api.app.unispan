from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Condition(Base):
    __tablename__ = "conditions"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for Fee
    fee = relationship(
                        "Fees",
                        order_by="fees.id",
                        back_populates="condition")

    # Relation for Devolution
    devolution = relationship(
                        "Devolution",
                        order_by="devolutions.id",
                        back_populates="condition")

    def __repr__(self):
        return '<Condition {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            enabled=self.enabled,
        )
