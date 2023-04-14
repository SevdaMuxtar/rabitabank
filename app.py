from flask import Flask

from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3307/rabita-bank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'secretkey123'

media_folder = 'static/uploads'
deposits_folder = 'static/media/deposits'
campaign_folder = 'static/media/campaign'
card_order_folder = 'static/media/card_order_icon'

ckeditor = CKEditor(app)

from extensions import *
from controllers import *
from models import *


if __name__ == '__main__':
   db.init_app(app)
   migrate.init_app(app)
   app.run(port=5000, debug=True)
