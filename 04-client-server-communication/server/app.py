#!/usr/bin/env python3
# 📚 Review With Students:
    # Validations
# Set up:
    #1. 

    # cd into server and run the following in Terminal
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=6000
        # flask db init
        # flask db revision --autogenerate -m'Create tables' 
        # flask db upgrade 
        # python seed.py
        # cd into client and run `npm install`

from flask import Flask, request, make_response, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound
from models import db, Production, CrewMember

#2. Import CORS from flask_cors, invoke it and pass it app
#Security feature that allows browser to enfore same origin policy
#Prevents scripts from accessing the domains resources
from flask_cors import CORS

#2. Running React Together 
    # Verify that gunicorn and honcho have been added to the pipenv
    #Honcho: https://honcho.readthedocs.io/en/latest/
    #Gunicorn: https://gunicorn.org/
    #Alternative for windows: https://docs.pylonsproject.org/projects/waitress/en/latest/ 
    # Create Procfile.dev in root
        # in Procfile.dev add:
            # web: PORT=3000 npm start --prefix client
            # api: gunicorn -b 127.0.0.1:6000 --chdir ./server app:app
        # In Terminal, cd into root and run:
            # `honcho start -f Procfile.dev`
    #Navigate to app.js
    

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


api = Api(app)


class Productions(Resource):

    def get(self):
        production_list = [p.to_dict() for p in Production.query.all()]
        response = make_response(
            production_list,
            200,
        )

        return response
    
    def post(self):
        data = request.get_json()
        new_production = Production(
            title=data['title'],
            genre=data['genre'],
            # budget=int(data['budget']),
            # image=request.form['image'],
            # director=request.form['director'],
            description=data['description'],
            # ongoing=bool(request.form['ongoing']),
        )

        db.session.add(new_production)
        db.session.commit()

        response_dict = new_production.to_dict()

        response = make_response(
            response_dict,
            201,
        )
        return response
api.add_resource(Productions, '/productions')

class ProductionByID(Resource):

    def get(self,id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            return handle_not_found(NotFound())
        
        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            200
        )
        
        return response


    def patch(self, id):
        production = Production.query.filter_by(id=id).first()

        if not production:
            abort(404, "The Production could not be found")

        data = request.get_json()
        for key in data:
            setattr(production, key, data[key])
        db.session.add(production)
        db.session.commit()

        production_dict = production.to_dict()

        response = make_response(
            production_dict, 200
        )

        return response
    

    def delete(self, id):
        production = Production.query.filter_by(id=id).first()

        if not production:
            abort(404, "The Production was not found")

        db.session.delete(production)
        db.session.commit()

        response = make_response("", 204)

        return response

   
api.add_resource(ProductionByID, '/productions/<int:id>')

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: Sorry the resource was not found", 404)
    return response


# To run the file as a script
# if __name__ == '__main__':
#     app.run(port=4000, debug=True)