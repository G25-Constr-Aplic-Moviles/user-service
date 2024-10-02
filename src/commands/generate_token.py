from .base_command import BaseCommannd
from ..models.user import User, GeneratedTokenUserJsonSchema
from ..session import Session
from ..errors.errors import Unauthorized, IncompleteParams, UserNotFoundError
import bcrypt


class GenerateToken(BaseCommannd):
    def __init__(self, data):
        if 'email' not in data or 'password' not in data:
            raise IncompleteParams()

        self.email = data['email']
        self.password = data['password']

    def execute(self):
        session = Session()

        if len(session.query(User).filter_by(email=self.email).all()) <= 0:
            session.close()
            raise UserNotFoundError()

        user = session.query(User).filter_by(email=self.email).one()

        if not self.valid_password(user.salt, user.password, self.password):
            session.close()
            raise UserNotFoundError()

        user.set_token()
        session.commit()

        user = GeneratedTokenUserJsonSchema().dump(user)
        session.close()

        return user

    def valid_password(self, salt, password, other_password):
        incoming_password = bcrypt.hashpw(
            other_password.encode('utf-8'), salt.encode('utf-8')
        ).decode()
        return incoming_password == password
