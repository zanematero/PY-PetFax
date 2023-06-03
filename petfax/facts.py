from flask import  Blueprint, render_template 

facts = Blueprint("facts", __name__, url_prefix="/facts")

@facts.route('/')
def index():
    return render_template('facts.html')