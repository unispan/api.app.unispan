from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Assigment(Base):
    __tablename__ = "assigments"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)

    # Equipment for Assigment
    equipment_id = Column(UUIDType(binary=False), ForeignKey('equipments.id'))
    equipment = relationship("Equipment", back_populates="assigment")

    delivery_date = Column(
                    DateTime,
                    default=datetime.datetime.now,
                    nullable=False)

    # Customer Project for Assigment
    customer_project_id = Column(
                            UUIDType(binary=False),
                            ForeignKey('customer_projects.id'))

    customer_project = relationship(
                            "CustomerProject",
                            back_populates="assigment")

    # Relation for Devolution
    devolution = relationship(
                        "Devolution",
                        order_by="devolutions.id",
                        back_populates="assigment")

    def __repr__(self):
        return '<Assigment {}|{}>'.format(self.id)

    def __json__(self):
        return dict(
            id=self.id,
            delivery_date=self.delivery_date,
            equipment=self.equipment,
            customer_project=self.customer_project,
        )
