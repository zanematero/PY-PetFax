from flask import ( Blueprint, render_template, request, redirect )
from . import models

facts = Blueprint("facts", __name__, url_prefix="/facts")

@facts.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        author = request.form['author']
        fact = request.form['fact']

        new_fact = models.fact(author=author,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()
        return redirect("/facts")
    
    results = models.fact.query.all()
    
    return render_template('facts/index.html', facts=results)

@facts.route('/new')
def new():
    return render_template('facts/new.html')