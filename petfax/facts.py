from flask import ( Blueprint, render_template, request, redirect )

facts = Blueprint("facts", __name__, url_prefix="/facts")

@facts.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        return redirect("/facts")
    return render_template('facts/index.html')

@facts.route('/new')
def new():
    return render_template('facts/new.html')