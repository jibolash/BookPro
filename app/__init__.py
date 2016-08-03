from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init(app)

	db.init_app(app)
	bootstrap.init_app(app)

	#register blueprints
	from .main import main
	app.register_blueprint(main)

	return app