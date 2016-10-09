from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class CustomerProject(Base):
    __tablename__ = "customer_projects"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)

    # Customer for Customer Projects
    customer_id = Column(UUIDType(binary=False), ForeignKey('customer.id'))
    customer = relationship("Customer", back_populates="cutomer_project")

    # Employee for Customer Projects
    employee_id = Column(UUIDType(binary=False), ForeignKey('employee.id'))
    employee = relationship("Employee", back_populates="cutomer_project")

    name = Column(String, unique=True, nullable=False)
    start_date = Column(DateTime,
                        default=datetime.datetime.now,
                        nullable=False)

    end_date = Column(DateTime, nullable=False)

    # Country for Customer Projects
    country_id = Column(UUIDType(binary=False), ForeignKey('countries.id'))
    country = relationship("Country", back_populates="cutomer_project")

    # Ubigeo for Customer Projects
    ubigeo_id = Column(UUIDType(binary=False), ForeignKey('ubigeo.id'))
    ubigeo = relationship("Ubigeo", back_populates="cutomer_project")

    house_number = Column(String, nullable=False)
    street_name = Column(String, nullable=False)

    # Relation for Assigment
    assigment = relationship(
                            "Assigments",
                            order_by="assigments.id",
                            back_populates="customer_project")

    # Relation for Schedule
    schedule = relationship(
                            "Schedule",
                            order_by="schedules.id",
                            back_populates="customer_project")

    def __repr__(self):
        return '<CustomerProject {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            customer=self.customer,
            employee=self.employee,
            start_date=self.start_date,
            end_date=self.end_date,
            country=self.country,
            ubigeo=self.ubigeo,
            house_number=self.house_number,
            street_name=self.street_name,
        )
