from flask import request
from app.models.admin_model import Owner
from app.models.movie_model import Movie
from app import db
from flask import make_response
from flask import json,jsonify

#singleton class
class Admin:
    instance = None
    def __init__(self):
        if Admin.instance is None:
            Admin.instance = self
        else:
            raise Exception("Only once created an object you can go with that instance")

    @staticmethod
    def get_instance():
        if Admin.instance is None:
            Admin.instance = Admin()
        return Admin.instance

    def home(self):
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify({'status':'success','Message':'Welcome'}),200,headers)

    def add_owner(self,request):
        email = request.json.get('email')
        password = request.json.get('password')
        owner_details = Owner(email,password)
        db.session.add(owner_details)
        db.session.commit()
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify({'status':'success','Message':'Record added succesfully'}),200,headers)

    def add_movie(self,request):
        #request.get_json()
        #print(type(y))
        email_id = request.json.get('email')
        movie_name = request.json.get('movie_name')
        movie_time=request.json.get('movie_time')
        theatre_name = request.json.get('theatre_name')
        owner_details = Owner.query.filter_by(email=email_id).first()
        if(owner_details is not None):
            print(owner_details.id)
            print(type(owner_details))
            movie_details = Movie(owner_details.id,movie_name, movie_time, theatre_name)
            db.session.add(movie_details)
            db.session.commit()
            headers = {"Content-Type": "application/json"}
            return make_response(jsonify({'status':'success','Message':'Record added successfully'}),200,headers)
        else:
            headers = {"Content-Type": "application/json"}
            return make_response(jsonify({'status':'failure','Message':'Something went wrong'}),500,headers)

    def get_details(self):
        #all_details = Movie.query.filter_by(movie_name ='Jagame Thandiram').first()
        #all_details = Movie.query.filter_by(movie_name ='Jagame Thandiram').one()
        #all_details= Movie.query.get(3)
        all_details = Movie.query.all()
        for row in all_details:
            print(row.movie_name)
            print(row.movie_time)
            print(row.theatre_name)
            print("\n")
            #if(all_details is not None):
            #print(all_details.movie_name)
            #all_details.movie_name = "hsjfhdlfndfakljflfncldzkjf"
            # db.session.commit()
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify({'status':'success','Message':'Fetch details successfully'}),200,headers)

    def owner_details(self,email):
        owner_details = Owner.query.filter_by(email=email).first()
        print(owner_details.theatres)
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify({'status':'success','Message':'successfully received'}),200,headers)

    def modify_details(self, request):
        email = request.json.get('email')
        name = request.json.get('name')
        theatre = request.json.get('theatre')
        updated_movie = request.json.get('update_movie')
        owner_details = Owner.query.filter_by(email=email).first()
        if(owner_details is not None):
            movie_details = Movie.query.filter_by(owner_id =owner_details.id , movie_name = name , theatre_name = theatre).first()
            if(movie_details is not None):
                movie_details.movie_name= updated_movie
                db.session.commit()
                headers = {"Content-Type": "application/json"}
                return make_response(jsonify({'status':'success','Message':'Modify details successfully'}),200,headers)
            else:
                headers = {"Content-Type": "application/json"}
                return make_response(jsonify({'status':'success','Message':'Something went wrong'}),400,headers)
        else:
            headers = {"Content-Type": "application/json"}
            return make_response(jsonify({'status':'error','Message':'Error'}),404,headers)

    def delete_movie(self,request):
        email = request.json.get('email')
        name = request.json.get('name')
        theatre = request.json.get('theatre')
        owner_details = Owner.query.filter_by(email=email).first()
        if owner_details is not None:
            movie_details = Movie.query.filter_by(owner_id = owner_details.id, movie_name= name, theatre_name= theatre).first()
            if movie_details is not None:
                db.session.delete(movie_details)
                db.session.commit()
                headers = {"Content-Type": "application/json"}
                return make_response(jsonify({'status':'success','Message':'delete details successfully'}),200,headers)
            else:
                headers = {"Content-Type": "application/json"}
                return make_response(jsonify({'status':'success','Message':'something went wrong'}),400,headers)
        else:
            headers = {"Content-Type": "application/json"}
            return make_response(jsonify({'status':'error','Message':'Error'}),404,headers)