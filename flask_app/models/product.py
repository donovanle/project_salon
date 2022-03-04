from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Product:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.time = data['time']
        self.category = data['category']
        self.user_id = data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def create_product(self,data):
        product = {
            'name' : data['name'],
            'price' : data['price'],
            'time' : data['time'],
            'category' : data['category'],
            'user_id' : data['users_id']
        }
        query = "INSERT INTO products (name, price, time,category, created_at, updated_at,users_id) VALUES (%(name)s,%(price)s,%(time)s,%(category)s, NOW(),NOW(),%(user_id)s);"
        return connectToMySQL('salon_schema').query_db(query, product)
    
    @classmethod
    def get_all_products(cls):
        query = "SELECT * FROM products ORDER by products.category;"
        results = connectToMySQL('salon_schema').query_db(query)
        products = []
        for item in results:
            products.append(cls(item))
            print(item)
        print(products)
        return products

    @classmethod
    def delete_product(cls,data):
        query= "DELETE FROM products WHERE id = %(product_id)s"
        return connectToMySQL('salon_schema').query_db(query, data)