from flask import (Flask,make_response,jsonify,request)
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost:3306/mtb'
db = SQLAlchemy(app)


from app.routes.admin_routes import router as admin_route
# Register blueprint(imported blueprint)
app.register_blueprint(admin_route)

@app.errorhandler(404)
def resource_not_found(error):
    headers = {'Content-Type': 'application/json'}
    return make_response(jsonify({'status':'failure','error':'page not found'}), 404,headers)

db.create_all()