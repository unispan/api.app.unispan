from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Position(Base):
    __tablename__ = "positions"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for employees
    employee = relationship(
                    "Employee",
                    order_by="employees.id",
                    back_populates="position")

    def __repr__(self):
        return '<Position {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            enabled=self.enabled,
        )
