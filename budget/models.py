from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
# from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

## Database setup
# # Get the current file's directory
# basedir = os.path.abspath(os.path.dirname(__file__))

# # Create the path to the database
# db_path = r'{}\..\data\budget.db'.format(basedir)
 
# # Create the SQLite engine using the absolute path
# engine = create_engine(f'sqlite:///{db_path}', echo=True)
# Base = declarative_base()

db = SQLAlchemy()

# Application Models
# Money In
class Income(db.Model):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    frequency = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Investments(db.Model):
    __tablename__ = 'investments'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Assets(db.Model):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Money Out
class Expense(db.Model):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    frequency = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Withholdings(db.Model):
    __tablename__ = 'withholdings'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    frequency = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


# # Create tables
# Base.metadata.create_all(engine)

# # Session setup
# Session = sessionmaker(bind=engine)
# session = Session()