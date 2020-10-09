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

def get_themes(subject_id):
    from models import Theme
    themes = session.query(Theme).filter(subject_id == subject_id).all()
    res = []
    for theme in themes:
        res.append(theme.name)
    return res

def get_template(id):
    from models import Template
    t = session.query(Template).filter(Template.id == id).first().text
    return t


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
