from flask import Flask
from config import config_options

def create_app(config_name):
  app=Flask(__name__)
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  app.config.from_object(config_options[config_name])

  from .request import configure_request
  configure_request(app)
  return app