from flask import Flask
from flask_migrate import Migrate
from models import db #, session
import os

# Local
from config import DevelopmentConfig, ProductionConfig, TestingConfig



def create_app():
    env = os.environ.get('FLASK_ENV', 'development')
    app = Flask(__name__, static_url_path='/static')

    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    return app