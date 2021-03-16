from flask import Flask, render_template
from flask_migrate import Migrate
import random

from .db import db
from app import models


migrate = Migrate()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'big!secret'
    db_name = "postgresdb"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://conveyor:admin123@postgres-service/{db_name}"
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        user = models.User(random.randint(1, 10000))
        db.session.add(user)
        db.session.commit()
        users = models.User.query.all()

        return render_template("base.html", users=users)

    return app
