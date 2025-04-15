
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Import models here to avoid circular import issues
    from . import models

    return app
