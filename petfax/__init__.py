from flask import Flask

def create_app():
    app = Flask("App")

    @app.route('/')
    def index():
        return "Hello this is PetFax!"

    @app.route('/pets')
    def pets_page():
        return "These are pets up for adoption"

    return app