from sqlalchemy import Boolean,Column,Integer, String
#we use "relationship" provided by SQLAlchemy ORM.
#This will become, more or less, a "magic" attribute that will contain the values from other tables related to this one.
from sqlalchemy.orm import relationship
from database import Base

class employee(Base):
    __tablename__ = "new_employee"

    id = Column(Integer, primary_key=True, index=True)
    ctc = Column(String)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    city = Column(String, unique=False)
    mobile = Column(String,unique= True)
    experience= Column(Integer)


#this is for Sqlite3
class Emp(Base):
    __tablename__ = "Emp"

    emp_id = Column(Integer ,primary_key=True,index=True,autoincrement=True)
    f_name= Column(String,unique=False, index=True)
    L_name=Column(String,unique=False, index=True)
    emp_age= Column(Integer,unique=False, index=True)
    city = Column(String,unique=False, index=True)
    ctc = Column(Integer, unique=False, index=True)
    Mobile = Column(Integer,unique=True, index=True)
    Experience = Column(Integer,unique=False, index=True)
