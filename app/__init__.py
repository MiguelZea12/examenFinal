from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate  # 🔥 Importar Flask-Migrate
from app.config import Config

# Inicializar Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar extensiones
api = Api(app)
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)  # 🔥 Configurar Flask-Migrate

# Importar y registrar Blueprints
from app.controller.users_controller import users_bp
from app.controller.auth_controller import auth_bp

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(auth_bp, url_prefix='/auth')
