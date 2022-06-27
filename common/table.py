from sqlalchemy import Column, Integer, String

from common.base import Base

class Users(Base):
  __tablename__ = "users"

  first_name = Column(String(255))
  last_name = Column(String(255))
  email = Column(String(255), primary_key=True)
  days_since_hired = Column(Integer)
  car = Column(String(255))
  dept = Column(String(255))