from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Fee(Base):
    __tablename__ = "fees"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)

    # Condition for Fee
    condition_id = Column(UUIDType(binary=False), ForeignKey('conditions.id'))
    condition = relationship("Condition", back_populates="fee")

    # Group for Fee
    group_id = Column(UUIDType(binary=False), ForeignKey('groups.id'))
    group = relationship("Group", back_populates="group")

    fee = Column(Float(precision=2), nullable=False)
    enabled = Column(Boolean, default=True)

    def __repr__(self):
        return '<Fee {}>'.format(self.id)

    def __json__(self):
        return dict(
            condition=self.condition,
            group=self.group,
            fee=self.fee,
            enabled=self.enabled,
        )
