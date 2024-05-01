from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, environ

# Create the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ.get("SECRET_KEY", "dev")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')

    create_database(app)

    return app

def create_database(app):
    if not path.exists(f"website/{DB_NAME}"):
        with app.app_context():
            db.create_all()
        print("Created Database!")