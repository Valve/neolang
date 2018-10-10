import os
import click
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config = None):
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
  app.config.from_object('config')
  db.init_app(app)
  migrate.init_app(app, db)
  register_blueprints(app)
  register_commands(app)
  CORS(app)
  return app

def register_blueprints(app):
  from neolang.api import api
  app.register_blueprint(api)

def register_commands(app):
  from neolang import commands
  app.cli.add_command(commands.seed)
  app.cli.add_command(commands.seed_entry_types)


