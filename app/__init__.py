from flask import Flask
from config import Config, Base
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5




app = Flask(__name__)

app.config.from_object(Config)
app.app_context().push()

db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)
bootstrap = Bootstrap5(app)


from app import routes, models

