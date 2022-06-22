from sqlalchemy import Boolean, Column,Integer, String

from.database import Base


class Employ(Base):
    __tablename__ = "empp"

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_age= Column(Integer,unique=True, index=True)
    CTC = Column(Integer, unique=True, index=True)


