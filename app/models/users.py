from app import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)

    def set_password(self, password):
        """Genera un hash de la contraseña"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica la contraseña"""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Convierte el objeto a diccionario"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
