from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Integer, String, Text, Column


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    tg_id = Column(String)
    username = Column(String)
    name = Column(String)
    last_dt = Column(String)

    def __init__(self, tg_id, username, name, last_dt):
        self.tg_id = tg_id
        self.username = username
        self.name = name
        self.last_dt = last_dt

class Symbol(Base):
    __tablename__ = 'symbol'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    level = Column(String)


class Unit(Base):
    __tablename__ = 'unit'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit = Column(String)
    level = Column(String)


class Equation(Base):
    __tablename__ = 'equation'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    equation = Column(String)
    level = Column(String)