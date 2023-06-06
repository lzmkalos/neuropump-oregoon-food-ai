#===: Import section
import os
from flask import (
    Flask,
    render_template,
    request,
    redirect
);
from flask_sqlalchemy import SQLAlchemy;
from flask_bcrypt import Bcrypt;

from .models import *;


#===: Setup :===
def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config['UPLOAD_FOLDER'] = 'static/employees'
        setup_db(app)


#===: Pre-Deploy :===
SECRET_KEY = os.urandom(32);

app = create_app();
bcrypt = Bcrypt(app);
app.config['SECRET_KEY'] = SECRET_KEY;


#===: Routes
@app.route('/')
def index():
    return render_template('index.html');