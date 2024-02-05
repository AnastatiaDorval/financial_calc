from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api 
from flask_sqlalchemy import SQLAlchemy
import calculations
from models import db, User, Contribution

class ContributionPercents(Resource): 
    def get(self):
        user = request.args.get('user')
        userDB = User.query.filter_by(username=user).all()
        if userDB:
            return f'{userDB[0].username} was found', 201
        else:
            return f"{user} was not found", 404
  
    # Corresponds to POST request 
    def post(self):
        new_user = User(username=request.args.get('user'), gross_income=None, income=None)
        db.session.add(new_user)
        db.session.flush()
        new_contributions = Contribution(
            roth_401k=float(request.args.get('roth')),
            after_tax=float(request.args.get('aftertax')),
            before_tax=float(request.args.get('pretax')),
            user_id=new_user.id
        )
        db.session.add(new_contributions)

        try:
            db.session.commit()
            return f'{request.args.get('user')} was successfully added', 201
        except:
            print('did not work')
            db.session.rollback()
            return f'{request.args.get('user')} was not added', 500
        
    def put(self):
        user_to_update = User.query.filter_by(username=request.args.get('user')).all()
        if user_to_update[0]:
            contributes = Contribution.query.filter_by(user_id=user_to_update[0].id).all()
            if contributes[0]:
                if request.args.get('roth'):
                    contributes[0].roth_401k = request.args.get('roth')
                if request.args.get('roth_ira'):
                    contributes[0].roth_ira = request.args.get('roth_ira')
                if request.args.get('before'):
                    contributes[0].before_tax = request.args.get('before')
                if request.args.get('after'):
                    contributes[0].after_tax = request.args.get('after')
                if request.args.get('broke'):
                    contributes[0].brokerage = request.args.get('broke')
                if request.args.get('trad_ira'):
                    contributes[0].traditional_ira = request.args.get('trad_ira')
                return f"{request.args.get('user')}'s contributions were updated", 201
            else:
                return f"{request.args.get('user')}'s contributions were not found", 500
        else:
            return f'{request.args.get('user')} was not found', 500
        # before_tax
        # after_tax
        # roth_401k
        # roth_ira
        # traditional_ira
        # brokerage
        
    
    def delete(self):
        user = request.args.get('user')
        user_to_delete = User.query.filter_by(username=user).all()
        if user_to_delete:
            db.session.delete(user_to_delete[0])
            db.session.commit()
            return f'{user} was found, and deleted', 201
        else:
            return f'{user} was not found', 500