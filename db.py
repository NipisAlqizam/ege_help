from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

eng = create_engine('sqlite:///ege_help.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=eng)
session = Session()

def get_subjects():
    from models import Subject
    subjects = session.query(Subject).all()
    res = []
    for subject in subjects:
        res.append(subject.name)
    return res


def init_db():
    import models
    Base.metadata.create_all(eng)

if __name__ == "__main__":
    import models
    init_db()
    print(get_subjects())
else:
    import models
    init_db()