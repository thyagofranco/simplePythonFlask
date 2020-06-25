from project import engine,Base
from project.models import Courses, Instructors, Classes, Users
from datetime import date
from sqlalchemy.orm import sessionmaker

#db.create_all()
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(Courses('CICD-Integração e Entrega Contínua',24))
session.commit()
