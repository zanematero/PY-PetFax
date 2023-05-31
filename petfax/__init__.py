from flask import Flask

def create_app():
    app = Flask("app")

    @app.route('/')
    def index():
        return "Hello this is PetFax!"

    # @app.route('/pets', method = ("GET"))
    # def pets_page():
    #     return "These are pets up for adoption"

    from .pet import bp
    app.register_blueprint(bp)
    
    return app