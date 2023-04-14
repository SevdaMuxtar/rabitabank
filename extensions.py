from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_migrate import Migrate
from flask_admin import Admin



db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app, name='Rabita Bank', template_mode='bootstrap3')
