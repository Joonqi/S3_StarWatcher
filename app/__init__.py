# __init__.py

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
   
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    env_config = os.getenv("APP_SETTINGS", 'config.DevelopmentConfig')
    app.config.from_object(env_config)


    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import (home_routes, star_routes, graph_routes, predict_routes)
    app.register_blueprint(home_routes.bp)
    app.register_blueprint(star_routes.bp)
    app.register_blueprint(graph_routes.bp)
    app.register_blueprint(predict_routes.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
