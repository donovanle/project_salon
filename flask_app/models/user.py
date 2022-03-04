from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def user_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s && password = %(password)s;"
        results = connectToMySQL('salon_schema').query_db(query,data)
        if results:
            return cls(results[0]) 
        return False
    
    @classmethod
    def validate_login(cls, data):
        user_validated = User.user_email(data)
        if not user_validated:
            flash("Invalid Email or Password","login")
            return False
        return True