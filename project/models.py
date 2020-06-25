from project import engine, Base
from sqlalchemy import ForeignKey,Column, Integer,String, Date
from sqlalchemy.orm import relationship

class Courses(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    duration = Column(Integer, nullable=False)


    def __init__(self,name=None,duration=None):
        self.name = name
        self.duration = duration

class Instructors(Base):

    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)

    def __init__(self,name=None):
        self.name = name

class Classes(Base):

    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    instructor_id = Column(Integer, ForeignKey('instructors.id'))
    users_id = Column(Integer, ForeignKey('users.id'))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)


    def __init__(self,instructor=None,start_date=None,end_date=None):
        self.instructor = instructor
        self.start_date = start_date
        self.end_date = end_date

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), unique=True, nullable=False)
    email = Column(String(length=50), unique=True, nullable=False)
    password = Column(String(length=50), nullable=False)
    courses = relationship('Classes')
    role = Column(String(length=50), default='user')

    def __init__(self, name=None, email=None,password=None,role=None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
