from app import app
from flask import render_template

@app.route('/')
@app.route('/index/<name>')

def index(name="Howdy, Pardner!"):
    return render_template("index.html", text=name)
