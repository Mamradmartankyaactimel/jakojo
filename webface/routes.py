from . import app
from flask import render_template


@app.route('/')
def index():
    pi=3.141519
    e=2.7
    title = 'Index'
    return render_template('base.html.j2', pi=pi, title=title)


@app.route('/info/')
def info():
    title = 'Info'
    return render_template('info.html.j2', title=title)
