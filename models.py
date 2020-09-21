from sqlalchemy import *
from sqlalchemy.orm import relationship
from db import Base

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    themes = relationship('Theme', back_populates='subject')
    
    def __repr__(self):
        return f'<Subject {self.name}>'

class Theme(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    subject = relationship('Subject', back_populates='themes')
    templates = relationship('Template', back_populates='theme')

class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    theme_id = Column(Integer, ForeignKey('themes.id'))

    theme = relationship('Theme', back_populates='templates')
