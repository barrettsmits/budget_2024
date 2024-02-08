import os

# Get the current file's directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the path to the database
db_path = r'{}\..\data\budget.db'.format(basedir)
 
# # Create the SQLite engine using the absolute path
# engine = create_engine(f'sqlite:///{db_path}', echo=True)

class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key'  # Important for security, use a random value

class ProductionConfig(Config):
    """Uses production database server."""
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    """Uses a development database server."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'

class TestingConfig(Config):
    """Uses a testing database server."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Example URI, change as needed
