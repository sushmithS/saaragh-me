from sqlalchemy import Boolean, Column,Integer, String

from database import Base


class Emp(Base):
    __tablename__ = "Emploee"

    emp_id = Column(Integer, primary_key=True, index=True)
    first_name= Column(String,unique=False, index=True)
    Last_name=Column(String,unique=False, index=True)
    emp_age= Column(Integer,unique=False, index=True)
    city = Column(String,unique=False, index=True)
    CTC = Column(Integer, unique=False, index=True)
    Mobile = Column(Integer,unique=True, index=True)
    Experience = Column(Integer,unique=False, index=True)
