from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Review:
    def __init__( self, data):
        self.id = data['id']
        self.name = data['name']
        self.rating = data['rating']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.appoitment_id = data['appoitment_id']
    @classmethod
    def create_review(self,data):
        reviews = {
            'name' : data['name'],
            'rating' : data['rating'],
            'description' : data['description'],
            'appoitment_id' : data['appoitment_id'],
        }
        query = "INSERT INTO reviews (name, rating, description,created_at, updated_at, appoitment_id) VALUES (%(name)s,%(rating)s,%(description)s,NOW(),NOW(),%(appoitment_id)s);"
        return connectToMySQL('salon_schema').query_db(query, reviews)
    
    @classmethod
    def all_reviews(cls):
        query = "SELECT * FROM reviews;"
        results = connectToMySQL('salon_schema').query_db(query)
        reviews = []
        for item in results:
            reviews.append(cls(item))
            print(item)
        print(reviews)
        return reviews