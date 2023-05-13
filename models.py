#===: Importing modules :===
import uuid;
from datetime import datetime;
from flask_sqlalchemy import SQLAlchemy;
from flask_migrate import Migrate;


#===: Importing section :==
from routes import *;
from server import db;


#===: Model User
class Costumer(db.Model):
    __tablename__ = 'costumer';
    id = db.Column(db.Integer(), primary_key=True, unique=True);
    name = db.Column(db.String(255), nullable=False, unique=False);
    type = db.Column(db.String(255), nullable=False, unique=False);
    commercial = db.Column(db.String(255), unique=False, nullable=False);
    schedule = db.Column(db.Datetime, default=datetime.utcnow(), nullable=False, unique=True);
    observation = db.Column(db.String(500), nullable=False, unique=True);
    def __init__(self, id, name, type, commercial, schedule, observation):
        self.id = id;
        self.name = name;
        self.type = type;
        self.commercial = commercial;
        self.schedule = datetime.utcnow();
        self.observation = observation;
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'commercial': self.commercial,
            'schedule': self.schedule,
            'observation': self.observation,
        };

class Product(db.Model):
    __tablename__ = 'product';
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"), unique=True);
    description = db.Column(db.Integer(), nullable=False, unique=False);
    quantity = db.Column(db.DateTime, default=datetime.utcnow());
    weight = db.Column(db.String(100), nullable=False);
    unit = db.Column(db.String(10), nullable=False);
    def __init__(self, id, quantityDollar):
        self.id = id;
        self.quantityDollar = quantityDollar;
        self.creationDate = datetime.utcnow();
    def serialize(self):
        return {
            'id': self.id,
            'quantityDollar': self.quantityDollar,
            'creationDate': self.creationDate,
        };

class Game(db.Model):
    __tablename__ = 'games';
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"), unique=True);
    name = db.Column(db.String(255), nullable=False);
    description = db.Column(db.Text, nullable=True);
    imageGame = db.Column(db.String(255), default=None);
    def __init__(self, id, name, description, imageGame):
        self.id = id;
        self.name = name;
        self.description = description;
        self.imageGame = imageGame;
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'imageGame': self.imageGame,
        };

class Deposit(db.Model):
    __tablename__ = 'deposit';
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"), unique=True);
    quantityDollar = db.Column(db.Integer(), nullable=False, unique=False);
    creationDate = db.Column(db.DateTime, default=datetime.utcnow());
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False);
    def __init__(self, id, quantityDollar):
        self.id = id;
        self.quantityDollar = quantityDollar;
        self.creationDate = datetime.utcnow();
    def serialize(self):
        return {
            'id': self.id,
            'quantityDollar': self.quantityDollar,
            'creationDate': self.creationDate,
        };


#===: Tables Auth
class LoginForm(FlaskForm):
    userEmail = StringField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Email"});
    userPass = PasswordField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Contraseña"});
    submit = SubmitField("Registrarse");
    def checkDatabaseRepetition(self, userAge, userNickname, userEmail):
        nicknameExists = Users.query.filter_by(nickname=userNickname.data).first();
        userEmailExists = Users.query.filter_by(email=userEmail.data).first();

class RegisterForm(FlaskForm):
    userFirstname = StringField(validators=[InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Nombre"});
    userLastname = StringField(validators=[InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Apellido"});
    userAge = StringField(validators=[InputRequired()], render_kw={"placeholder": "Edad"});
    userNickname = StringField(validators=[InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Nickname"});
    userEmail = StringField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Email"});
    userPass = PasswordField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Contraseña"});
    submit = SubmitField("Registrarse");
    def checkDatabaseRepetition(self, userAge, userNickname, userEmail):
        nicknameExists = Users.query.filter_by(nickname=userNickname.data).first();
        userEmailExists = Users.query.filter_by(email=userEmail.data).first();
        if userAge < 18:
            raise ValidationError("Lo lamentamos, para poder crear una cuenta debes ser mayor de edad.");
        if nicknameExists:
            raise ValidationError("El nickname ya existe. Inténtalo de nuevo con uno distinto.");
        if userEmailExists:
            raise ValidationError("El correo ya se encuentra asociado a otra cuenta. Inténtalo de nuevo con uno distinto.");