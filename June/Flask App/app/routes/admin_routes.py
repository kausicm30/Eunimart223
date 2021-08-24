from flask import (Flask,Blueprint, request,jsonify,abort)
from flask.helpers import make_response
from flask_json_schema import (JsonSchema, JsonValidationError)
from app import app
from app.services.admin_service.admin_services import Admin
from app.utils.logger import logging
from app.utils.validators.admin_schema import admin_schema
schema = JsonSchema(app)



#Create a admin object
admin = Admin()

# admin blueprint
router = Blueprint('adminRoute', __name__, url_prefix='/admin')


#Home
@router.route('/')
def home():
    return admin.home()

#add owners
@router.route('/add_owner', methods=['POST'])
@schema.validate(admin_schema['owner_schema'])
def add_owner():
    return admin.add_owner(request)

#add Details
@router.route('/add_movie', methods=['POST'])
@schema.validate(admin_schema['add_movie_schema'])
def add_movie():
    return admin.add_movie(request)

#display details
@router.route('/display_details', methods=['GET'])
def get_details():
    return admin.get_details()

#display owner details
@router.route('/owner_details', methods=['GET'])
def owner_details():
    return admin.owner_details(request.args.get('email'))

# Update Details
@router.route('/modify_details', methods=['POST'])
@schema.validate(admin_schema['modify_movie_schema'])
def modify_details():
    return admin.modify_details(request)


# delete details
@router.route('/delete_movie', methods=['POST'])
@schema.validate(admin_schema['delete_movie_schema'])
def delete_movie():
    return admin.delete_movie(request)

@router.errorhandler(JsonValidationError)
def validation_error(e):
    headers={'Content-Type': 'application/json'}
    return make_response(jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]}),400,headers)

