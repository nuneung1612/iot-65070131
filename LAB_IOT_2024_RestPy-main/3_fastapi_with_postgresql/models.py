from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    stu_id = Column(String, index=True)
    fname = Column(String, index=True)
    lname = Column(String, index=True)
    dob = Column(String, index=True)
    gender = Column(String, index=True)