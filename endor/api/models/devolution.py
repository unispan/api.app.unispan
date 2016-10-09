from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Devolution(Base):
    __tablename__ = "devolution"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)

    # Assigment for Devolution
    assigment_id = Column(UUIDType(binary=False), ForeignKey('assigments.id'))
    assigment = relationship("Assigment", back_populates="devolution")

    # Condition for Devolution
    condition_id = Column(UUIDType(binary=False), ForeignKey('conditions.id'))
    condition = relationship("Condition", back_populates="devolution")

    fee = Column(Float(precision=2), nullable=False)

    devolution_date = Column(
                        DateTime,
                        default=datetime.datetime.now,
                        nullable=False)

    def __repr__(self):
        return '<Devolution {}>'.format(self.id)

    def __json__(self):
        return dict(
            id=self.id,
            assigment=self.assigment,
            condition=self.condition,
            fee=self.fee,
            devolution_date=self.devolution_date,
        )
