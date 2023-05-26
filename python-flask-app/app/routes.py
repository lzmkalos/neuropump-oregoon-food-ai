#===: Import section
from app import app, bcrypt, db;
import models as md;
from flask import (
    Flask,
    render_template,
    request,
    redirect
);


#===: Views
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html');