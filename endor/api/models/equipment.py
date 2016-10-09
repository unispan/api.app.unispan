from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Equipment(Base):
    __tablename__ = "equipments"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)

    # Group for Equipment
    group_id = Column(UUIDType(binary=False), ForeignKey('groups.id'))
    group = relationship("Group", back_populates="equipment")

    name = Column(String, nullable=False)
    weight = Column(Float(precision=2), nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for Assigment
    assigment = relationship(
                            "Assigment",
                            order_by="assigments.id",
                            back_populates="equipment")


    def __repr__(self):
        return '<Equipment {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            weight=self.weight,
            group=self.group,
            enabled=self.enabled,
        )
