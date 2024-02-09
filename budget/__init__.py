from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# local imports
from .models import db
from .routes import bp as main_blueprint
from .config import DevelopmentConfig, ProductionConfig, TestingConfig

# global variable
env = os.environ.get('FLASK_ENV', 'development')


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Load configuration
    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Initialize extensions with app
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_blueprint)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return "Page not found", 404

    @app.errorhandler(500)
    def internal_error(error):
        return "Internal server error", 500

    # Additional setup like logging, additional blueprints, etc.
    # ...
    Migrate(app, db)

    return app