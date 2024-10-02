from .base_command import BaseCommannd
from ..models.user import User, UserSchema, CreatedUserJsonSchema
from ..session import Session
from ..errors.errors import IncompleteParams, UserAlreadyExists
from sqlalchemy import or_


class CreateUser(BaseCommannd):
    def __init__(self, data):
        self.data = data

    def execute(self):
        try:
            posted_user = UserSchema(
                only=('firstName', 'lastName', 'email', 'password')
            ).load(self.data)
            user = User(**posted_user)
            session = Session()

            if self.email_exist(session, self.data['email']):
                session.close()
                raise UserAlreadyExists()

            session.add(user)
            session.commit()

            new_user = CreatedUserJsonSchema().dump(user)
            session.close()

            return new_user
        except TypeError:
            raise IncompleteParams()

    def email_exist(self, session, email):
        return session.query(User).filter_by(email=email).count() > 0
