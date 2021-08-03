# __init__.py

import os
from rq import Queue
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fmjxhhfddaofdq:51daa2f796d1167916c3348865ed4175d80087fcac50255f33907f5fd7da6ea9@ec2-44-194-145-230.compute-1.amazonaws.com:5432/d6lbt10a3usids'
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:qwerqwer@localhost:5432/watchapp"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    env_config = os.getenv("APP_SETTINGS", 'config.StagingConfig')
    app.config.from_object(env_config)


    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import (home_routes, star_routes, graph_routes, predict_routes)
    app.register_blueprint(home_routes.bp)
    app.register_blueprint(star_routes.bp)
    app.register_blueprint(graph_routes.bp)
    app.register_blueprint(predict_routes.bp)

    from worker import conn
    from utils import count_words_at_url
    q = Queue(connection=conn)
    result=q.enqueue(count_words_at_url, 'http://heroku.com')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
