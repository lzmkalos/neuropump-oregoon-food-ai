#===: Import section
from server import app, bcrypt, db;
import models as md;

from flask import (
    Flask,
    render_template,
    request,
    redirect
);
from flask_login import (
    UserMixin, 
    login_user, 
    LoginManager, 
    login_required, 
    logout_user,
    current_user
);
from flask_wtf import FlaskForm;
from wtforms import StringField, PasswordField, SubmitField;
from wtforms.validators import InputRequired, Length, ValidationError;


#===: Views
@app.route('/')
def index():
    return render_template('index.html');

@app.route('/login')
def login():
    return render_template('auth/login.html');

@app.route('/register')
def register():
    form = md.RegisterForm();
    if form.validate_on_submit():
        hashedPass = bcrypt.generate_password_hash(form.userpass.data).decode('utf-8');
        newUser = md.User(username=form.username.data, userpass=hashedPass, userBank=0);
        print(newUser);
        db.session.add(newUser);
        db.session.commit();
        db.session.close();
        return redirect(md.url_for('login'));
    return render_template('auth/register.html', form=form);

@app.route('/home')
def home():
    return "Home";

@app.route('/config')
def config():
    return "Config";

@app.route('/roulette')
def roulette():
    return "Roulette";

@app.route('/slots')
def slots():
    return "Slots";

@app.route('/logout')
def logout():
    return "Logout";

@app.route('/delete/<string:id>')
def deleteUser():
    return "Delete user";