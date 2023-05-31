from flask import Flask

app = Flask("App")

@app.route('/')
def index():
    return "Hello this is PetFax!"

@app.route('/pets')
def pets_page():
    return "These are pets up for adoption"