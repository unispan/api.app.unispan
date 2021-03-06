from endor.api.models import Base
import datetime, uuid
from slugify import slugify
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import UUIDType
from sqlalchemy_utils.decorators import generates


class Role(Base):
    __tablename__ = "roles"
    id = Column(UUIDType(binary=False), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    # Relation for user
    user = relationship(
                    "User",
                    order_by="users.id",
                    back_populates="role")

    def __repr__(self):
        return '<Role {}|{}>'.format(self.id, self.name)

    def __json__(self):
        return dict(
            id=self.id,
            name=self.name,
            enabled=self.enabled,
        )
