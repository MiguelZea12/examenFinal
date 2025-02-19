from app import ma
from app.models.users import User
from marshmallow import fields, validate

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password_hash",)  # No exponer el hash de la contraseña

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    email = fields.Email(required=True, validate=validate.Length(max=120))
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)
