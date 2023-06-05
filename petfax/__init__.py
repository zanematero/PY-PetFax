from flask import Flask
from . import ( pet, facts )
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()
def create_app(): 
  app = Flask(__name__)
  
  app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("uri_string")
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  
  from . import models
  models.db.init_app(app)

  migrate = Migrate(app, models.db)

  app.register_blueprint(pet.bp)
  app.register_blueprint(facts.facts)  

  @app.route('/')
  def hello(): 
    return 'Welcome to PetFax!'

  return app