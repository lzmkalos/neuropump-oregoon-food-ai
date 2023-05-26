#===: Import section
import os
from flask  import Flask;
from flask_sqlalchemy import SQLAlchemy;
from flask_bcrypt import Bcrypt;


#===: Setup :===
db = SQLAlchemy();
dbConfig = "postgresql://postgres@localhost:5432/dev_tumi_db";


def create_app():
    app_ = Flask(
        __name__,
        template_folder='templates',
        static_folder='static'
    );
    app_.config['SQLALCHEMY_DATABASE_URI'] = dbConfig;
    app_.config["TEMPLATES_AUTO_RELOAD"] = True
    db.init_app(app_);
    with app_.app_context():
        db.create_all();
    return app_;


#===: Pre-Deploy :===
SECRET_KEY = os.urandom(32);

app = create_app();
bcrypt = Bcrypt(app);
app.config['SECRET_KEY'] = SECRET_KEY;


#===: Deploy :===
if __name__ == '__main__':
    from models import *;
    app.run(debug=True);