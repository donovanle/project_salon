from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Reserve:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.date = data['date']
        self.product_id = data['product_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def new_reserve(self, data):
        reserve = {  
            'name' : data['name'],
            'email' : data['email'],
            'date' : data['date'],
            'product_id' : data['product_id'],
        }
        query = "INSERT INTO appoitments (name, email,date,product_id, created_at, updated_at) VALUES(%(name)s,%(email)s,%(date)s,%(product_id)s,NOW(),NOW());"
        return connectToMySQL('salon_schema').query_db(query, reserve)
    
    @classmethod
    def all_reserves(cls):
        query = "SELECT * FROM appoitments;"
        results = connectToMySQL('salon_schema').query_db(query)
        appoint = []
        for item in results:
            appoint.append(cls(item))
            print(item)
        print(appoint)
        return appoint
    
    @classmethod
    def delete_reserve(cls,data):
        query= "DELETE FROM appoitments WHERE id = %(appoitment_id)s"
        return connectToMySQL('salon_schema').query_db(query, data)