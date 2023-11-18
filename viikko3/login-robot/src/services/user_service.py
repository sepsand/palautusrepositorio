from entities.user import User
import re
import sys, pdb

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        # pysäytetään ohjelman suoritus tälle riville
        pdb.Pdb(stdout=sys.__stdout__).set_trace()

        if not username or not password:
            raise UserInputError("Username and password are required")

        # username length must be at least 3
        if len(username) < 3:
            raise UserInputError("Invalid username")
        
        # username must consist of characters a-z
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Invalid username")
        
        # password length must be at least 8
        if len(password) < 8:
            raise UserInputError("Invalid password")
        
        # password must consist of characters a-z and digits 0-9
        if not ( re.search("[a-z]+", password) and
                 re.search("[0-9]+", password)     ):
            raise UserInputError("Invalid password")
        


