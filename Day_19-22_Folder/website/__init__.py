from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'   # We comfigure a new Database conncection using SQLAlchemy and SQLite. 
    db.init_app(app)

    from .views import my_view
    app.register_blueprint(my_view)

    from .models import Todo
    with app.app_context():
        db.create_all()

    return app