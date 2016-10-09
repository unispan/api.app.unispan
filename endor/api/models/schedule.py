from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)

    schedule_date = Column(
                        DateTime,
                        default=datetime.datetime.now,
                        nullable=False)

    # Customer Project for Schedule
    customer_project_id = Column(UUIDType(binary=False), ForeignKey('cutomer_projects.id'))
    customer_project = relationship("CustomerProject", back_populates="schedule")

    # Schedule Windows for Schedule
    schedule_window_id = Column(UUIDType(binary=False), ForeignKey('schedule_windows.id'))
    schedule_window = relationship("ScheduleWindow", back_populates="schedule")

    enabled = Column(Boolean, default=True)


    def __repr__(self):
        return '<Schedule {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            schedule_date=self.schedule_date,
            customer_project=self.customer_project,
            schedule_window=self.schedule_window,
            enabled=self.enabled,
        )
