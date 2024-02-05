from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api 
from flask_sqlalchemy import SQLAlchemy
import calculations
from models import db, User

class GrossPay(Resource):

    ########################################################
    # receives user
    # returns user info
    ########################################################
    def get(self):
        user = request.args.get('user')
        userDB = User.query.filter_by(username=user).all()
        if userDB:
            return userDB.gross_income, 201
        else:
            return f"{user} was not found", 404
        
    ########################################################
    # receives user, gross pay, pay after taxes
    # returns message
    ########################################################
    def post(self):
        user = request.args.get('user')
        user_update = User.query.filter_by(username=user).all()
        if user_update[0]:
            user_update.gross_income = request.args.get('pretax')
            db.session.commit()
            return f'{user} was found and updated', 201
        else:
            return f'{user} was not found', 404
    
    def put(self):
        user_to_update = User.query.filter_by(username=request.args.get('user')).all()
        if user_to_update[0]:
            update = user_to_update[0]
            if request.args.get('income'):
                update.income = request.args.get('income')
            if request.args.get('gross_income'):
                update.gross_income = request.args.get('gross_income')
            db.session.commit()
            return f"{request.args.get('user')}'s info was updated", 201
        else:
            return f"{request.args.get('user')} was not found", 500
    
    ########################################################
    # receives user
    # returns message
    ########################################################
    def delete(self):
        user = request.args.get('user')
        userDB = User.query.filter_by(username=user)
        if userDB:
            db.session.delete(userDB)
            db.session.commit()
            return f"{user} was removed", 201
        else:
            return f"{user} could not be found", 404