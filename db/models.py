from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Integer, String, Text, Column


Base = declarative_base()


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