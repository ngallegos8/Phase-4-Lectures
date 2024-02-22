#!/usr/bin/env python3
# 📚 Review With Students:
    # Validations
    # REST
    # Status codes
    # Error handling 
    
# Set up:
    # cd into server and run the following in the terminal
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5000
    # flask db init
    # flask db revision --autogenerate -m'Create tables' or flask db migrate -m "created tables"
    # flask db upgrade 
    # python seed.py
from flask import Flask, request, make_response, abort, jsonify
from flask_migrate import Migrate
# 1.✅ Import NotFound from werkzeug.exceptions for error handling
from werkzeug.exceptions import NotFound

#2. ✅ Import `Api` and `Resource` from `flask_restful`
    # ❓ What do these two classes do at a higher level?  API: allows to add controller to route. Resource: allows class to inherit resource
from flask_restful import Api, Resource


from models import db, Production, CrewMember
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)

from models import db, Production
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)

#3. Initialize the Api
    # `api = Api(app)`
api = Api(app)

#4. Create a Production class that inherits from Resource
class Productions(Resource):

#5. Create a GET (All) Route
    # 4.1 Make a `get` method that takes `self` as a param.
    # 4.2 Create a `productions` array.
    # 4.3 Make a query for all productions. For each `production`, create a dictionary 
    # containing all attributes before appending to the `productions` array.
    # 4.4 Create a `response` variable and set it to: 
    #  #make_response(
    #       jsonify(productions),
    #       200
    #  )
    # 4.5 Return `response`.
    # 4.6 After building the route, run the server and test in the browser.
    def get(self):
        production = [product.to_dict() for product in Production.query.all()]
        # production = [product.to_dict(only=("description", )) for product in Production.query.all()]      #ONLY
        # production = [product.to_dict(rules=("-crew-members", )) for product in Production.query.all()]       #RULES - SERIALIZATION
        print(production)

        return make_response(production, 200)
        # return make_response(jsonify(production), 200) #OR...
        # return production, 200 #OR...
    
    def post(self):
        new_production = Production(
            title = request.form["title"],
            genre = request.form["genre"],
            budget = float(request.form["budget"]),
            image = request.form["image"],
            director = request.form["director"],
            description = request.form["description"],
            ongoing = bool(request.form["ongoing"])
        )
        db.session.add(new_production)
        db.session.commit()

        return new_production.to_dict(), 201

api.add_resource(Productions, "/productions")

#5. Use our serializer to format our response to be cleaner
    # 10.1 Query all of the productions, convert them to a dictionary with `to_dict` before setting them to a list.
    # 10.2 Invoke `make_response`, pass it the production list along with a status of 200. Set `make_response` to a 
    # `response` variable.
    # 10.3 Return the `response` variable.
    # 10.4 After building the route, run the server and test your results in the browser.
 
#6. Create a POST Route
    # Prepare a POST request in Postman. Under the `Body` tab, select `form-data` and fill out the body 
    # of a production request. 
    
    # Create the POST route 
    # 📚 Review With Students: request object
    # 11.1 Create a `post` method and pass it `self`.
    # 11.2 Create a new production from the `request.form` object.
    # 11.3 Add and commit the new production.
    # 11.4 Convert the new production to a dictionary with `to_dict`
    # 11.5 Set `make_response` to a `response` variable and pass it the new production along with a status of 201.
    # 11.6 Test the route in Postman.

   
#7. Add the new route to our api with `api.add_resource`

class ProductionById(Resource):

#8. Create a GET (One) route
    # 13.1 Build a class called `ProductionByID` that inherits from `Resource`.
    # 13.2 Create a `get` method and pass it the id along with `self`. (This is how we will gain access to 
    # the id from our request)
    # 13.3 Make a query for our production by the `id` and build a `response` to send to the browser.
    def get(self, id):
        production = Production.query.filter(Production.id == id).first()
        if not production:
            abort(404, "The production was not found")
        
        return production.to_dict(), 200
    
    
    
    

#9. Add the new route to our api with `api.add_resource`

#10. If a production is not found raise the NotFound exception
    # 3.1 AND/OR use abort() to create a 404 with a customized error message

#11.Patch
    # 4.1 Create a patch method that takes self and id
    # 4.2 Query the Production from the id
    # 4.3 If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    # 4.4 Loop through the request.form object and update the productions attributes. Note: Be cautions of the data types to avoid errors.
    # 4.5 add and commit the updated production 
    # 4.6 Create and return the response
    def patch(self, id):
            production = Production.query.filter(Production.id == id).first()
            if not production:
                abort(404, "Production not found")
            
            data = request.get_json()
            for key in data:
                setattr(production, key, data[key])
            
            db.session.add(production)
            db.session.commit()

            return production.to_dict(), 202
  
#12. Delete
    # 5.1 Create a delete method, pass it self and the id
    # 5.2 Query the Production 
    # 5.3 If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    # 5.4 delete the production and commit 
    # 5.5 create a response with the status of 204 and return the response 
    def delete(self, id):
        production = Production.query.filter(Production.id == id).first()
        if not production:
            # abort(404, "Production not found")
            return handle_not_found(NotFound())
        
        db.session.delete(production)
        db.session.commit()

        return {}, 204

    
api.add_resource(ProductionById, '/productions/<int:id>')


#13. Use the @app.errorhandler() decorator to handle Not Found   ## DYNAMIC compared to 'ABORT'
    # 2.1 Create the decorator and pass it NotFound
    # 2.2 Use make_response to create a response with a message and the status 404
    # 2.3 return the response
@app.errorhandler(NotFound)
def handle_not_found(e):
    return make_response("Not Found: The resource was not found", 404)

app.register_error_handler(404, handle_not_found)
    
# To run the file as a script
if __name__ == '__main__':
    app.run(port=4000, debug=True)