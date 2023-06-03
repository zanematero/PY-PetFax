from flask import Flask
from . import ( pet, facts )

def create_app(): 
  app = Flask(__name__)
  
  app.register_blueprint(pet.bp)
  app.register_blueprint(facts.facts)  

  @app.route('/')
  def hello(): 
    return 'Welcome to PetFax!'

  return app