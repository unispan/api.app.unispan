from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Weekday(Base):
    __tablename__ = "weekdays"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for Schedule Window
    schedule_window = relationship(
                            "ScheduleWindow",
                            order_by="schedule_windows.id",
                            back_populates="weekday")

    def __repr__(self):
        return '<weekday {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            enabled=self.enabled,
        )
