from flask import Flask
from flask_migrate import Migrate
from .config import config_options
from .models import db

from app.home import home_routes
from app.cars import cars_routes


def create_app(config_type):
    app = Flask(__name__)
    current_config = config_options[config_type]
    print(current_config)
    app.config.from_object(current_config)
    
    
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    migrate = Migrate(app=app, db=db)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(cars_routes)

    app.register_blueprint(home_routes)
    return app