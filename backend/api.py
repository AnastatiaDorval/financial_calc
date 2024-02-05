from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

from models import db, User, Contribution

from endpoints.contributions import ContributionPercents
from endpoints.income import GrossPay
  
# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:financialGURU@172.20.0.2:5432/financial_calc'
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
app.config['SQLALCHEMY_ECHO'] = True

# adding the defined resources along with their corresponding urls 
api.add_resource(ContributionPercents, '/401K/percents')
api.add_resource(GrossPay, '/pay')

with app.app_context():
    db.init_app(app)
    db.create_all()
    print('Tables created?')
    db.session.commit()
    print('Ran commit')

# driver function 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug = True) 