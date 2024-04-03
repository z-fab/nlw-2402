from src.models.settings.base import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func

class Check_ins(Base):
    __tablename__ = 'check_ins'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey('attendees.id'))

    def __repr__(self):
        return f'<CheckIn [id={self.id}, attendeeId={self.attendeeId}, created_at={self.created_at}]>'