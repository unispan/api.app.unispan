from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class ScheduleWindow(Base):
    __tablename__ = "schedule_windows"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)

    # Weekday for Schedule Window
    weekday_id = Column(Integer, ForeignKey('weekdays.id'))
    weekday = relationship("Weekday", back_populates="schedule_window")

    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for Schedule
    schedule = relationship(
                            "Schedule",
                            order_by="schedules.id",
                            back_populates="schedule_window")

    def __repr__(self):
        return '<ScheduleWindow {}>'.format(self.id)

    def __json__(self):
        return dict(
            id=self.id,
            weekday=self.weekday,
            start_time=self.start_time,
            end_time=self.end_time,
            enabled=self.enabled,
        )
