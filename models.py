from sqlalchemy import Boolean, Column,Integer, String ,ForeignKey
#we use "relationship" provided by SQLAlchemy ORM.
#This will become, more or less, a "magic" attribute that will contain the values from other tables related to this one.
from sqlalchemy.orm import relationship
from database import Base


class Emp(Base):
    __tablename__ = "Emp"

    emp_id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    f_name= Column(String,unique=False, index=True)
    L_name=Column(String,unique=False, index=True)
    emp_age= Column(Integer,unique=False, index=True)
    city = Column(String,unique=False, index=True)
    ctc = Column(Integer, unique=False, index=True)
    Mobile = Column(Integer,unique=True, index=True)
    Experience = Column(Integer,unique=False, index=True)

