from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

## Database setup
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