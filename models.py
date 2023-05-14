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
    coordinates = db.Column(db.Float(), nullable=False, unique=True);
    zone = db.Column(db.Integer(), nullable=False, unique=True);
    def __init__(self, id, name, type, commercial, schedule, observation, coordinates, zone):
        self.id = id;
        self.name = name;
        self.type = type;
        self.commercial = commercial;
        self.schedule = schedule;
        self.observation = observation;
        self.coordinates = coordinates;
        self.zone = zone;
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'commercial': self.commercial,
            'schedule': self.schedule,
            'observation': self.observation,
            'coordinates': self.coordinates,
            'zone': self.zone,
        };

class Product(db.Model):
    __tablename__ = 'product';
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"), unique=True);
    description = db.Column(db.Integer(), nullable=False, unique=False);
    quantity = db.Column(db.Integer(), nullable=False, unique=False);
    weight = db.Column(db.Integer(), nullable=False, unique=False);
    unit = db.Column(db.String(10), nullable=False, unique=False);
    def __init__(self, id, description, quantity, weight, unit):
        self.id = id;
        self.description = description;
        self.quantity = quantity;
        self.weight = weight;
        self.unit = unit;
    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'quantity': self.quantity,
            'weight': self.weight,
            'unit': self.unit,
        };

class Vehicle(db.Model):
    __tablename__ = 'vehicle';
    license_plate = db.Column(db.String(6), primary_key=True, unique=True);
    capacity = db.Column(db.Float(), nullable=False);
    volume = db.Column(db.Float(), nullable=False);
    supplier = db.Column(db.String(255), default=None);
    type = db.Column(db.String(255), default=None);
    legalName = db.Column(db.String(255), default=None);
    def __init__(self, license_plate, capacity, volume, supplier, type, legalName):
        self.license_plate = license_plate;
        self.capacity = capacity;
        self.volume = volume;
        self.supplier = supplier;
        self.type = type;
        self.legalName = legalName;
    def serialize(self):
        return {
            'license_plate': self.license_plate,
            'capacity': self.capacity,
            'volume': self.volume,
            'supplier': self.supplier,
            'type': self.type,
            'legalName': self.legalName,
        };

class Order(db.Model):
    __tablname__ = 'order';
    id = db.Column(db.String(255), primary_key=True, nullable=False);
    totalWeight = db.Column(db.Float(), nullable=False);
    unit = db.Column(db.String(10), nullable=False);
    date = db.Column(db.Datetime, default=datetime.utcnow(), nullable=False, unique=False);
    def __init__(self, id, totalWeight, unit):
        self.id = id;
        self.totalWeight = totalWeight;
        self.unit = unit;
        self.date = datetime.utcnow();
    def serialize(self):
        return {
            'id': self.id,
            'totalWeight': self.quantityDollar,
            'unit': self.creationDate,
            'date': self.date
        };

class Route(db.Model):
    __tablename__ = 'route';
    orderID = db.Column(db.String(255), db.ForeignKey('order.id'), nullable=False);
    posStart = db.Column(db.Float(), nullable=False, unique=False);
    postEnd = db.Column(db.Float(), nullable=False, unique=False);
    def __init__(self, posStart, posEnd):
        self.posStart = posStart;
        self.posEnd = posEnd;
    def serialize(self):
        return {
            'id': self.id,
            'posStart': self.posStart,
            'posEnd': self.posEnd,
        };

#===: Tables Auth
class LoginForm(FlaskForm):
    userEmail = StringField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Email"});
    userPass = PasswordField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Contraseña"});
    submit = SubmitField("Registrarse");
    def checkDatabaseRepetition(self, userAge, userNickname, userEmail):
        nicknameExists = Costumer.query.filter_by(nickname=userNickname.data).first();
        userEmailExists = Costumer.query.filter_by(email=userEmail.data).first();

class RegisterForm(FlaskForm):
    userFirstname = StringField(validators=[InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Nombre"});
    userLastname = StringField(validators=[InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Apellido"});
    userAge = StringField(validators=[InputRequired()], render_kw={"placeholder": "Edad"});
    userNickname = StringField(validators=[InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Nickname"});
    userEmail = StringField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Email"});
    userPass = PasswordField(validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Contraseña"});
    submit = SubmitField("Registrarse");
    def checkDatabaseRepetition(self, userAge, userNickname, userEmail):
        nicknameExists = Costumer.query.filter_by(nickname=userNickname.data).first();
        userEmailExists = Costumer.query.filter_by(email=userEmail.data).first();
        if userAge < 18:
            raise ValidationError("Lo lamentamos, para poder crear una cuenta debes ser mayor de edad.");
        if nicknameExists:
            raise ValidationError("El nickname ya existe. Inténtalo de nuevo con uno distinto.");
        if userEmailExists:
            raise ValidationError("El correo ya se encuentra asociado a otra cuenta. Inténtalo de nuevo con uno distinto.");