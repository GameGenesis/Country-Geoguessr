from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import environ, path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = environ.get("SECRET_KEY", "dev")
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import User

    create_database(app)

    return app

def create_database(app):
    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)