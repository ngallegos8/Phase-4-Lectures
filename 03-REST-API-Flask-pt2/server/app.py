#!/usr/bin/env python3
# 📚 Review With Students:
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
from flask import Flask, request, make_response, abort
from flask_migrate import Migrate
# 1.✅ Import NotFound from werkzeug.exceptions for error handling
#2. ✅ Import `Api` and `Resource` from `flask_restful`
    # ❓ What do these two classes do at a higher level? 


from models import db, Production, CrewMember
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)


#3. Initialize the Api
    # `api = Api(app)`

#4. Create a Production class that inherits from Resource

#5. Create a GET (All) Route
    #Create a `productions` array.
    #Make a query for all productions. For each `production`, create a dictionary 
    # containing all attributes before appending to the `productions` array.
    #Create a `response` variable and set it to: 
    #  #make_response(
    #       jsonify(productions),
    #       200
    #  )
    #Return `response`.
    #After building the route, run the server and test in the browser.
    #Use our serializer to format our response to be cleaner
 
#6. Create a POST Route.
    #Create a new production from the `request.form` object.
    #Add and commit the new production.
    #Convert the new production to a dictionary with `to_dict`
    #Set `make_response` to a `response` variable and pass it the new production along with a status of 201.
    #Test the route in Postman.

   
#7. Add the new route to our api with `api.add_resource`

#8. Create a GET (One) route
    #Build a class called `ProductionByID` that inherits from `Resource`.
    #Create a `get` method and pass it the id along with `self`. (This is how we will gain access to 
    # the id from our request)
    #Make a query for our production by the `id` and build a `response` to send to the browser.


#9. Add the new route to our api with `api.add_resource`

#10. If a production is not found raise the NotFound exception
    #AND/OR use abort() to create a 404 with a customized error message

#11.Patch
    #Create a patch method that takes self and id
    #Query the Production from the id
    #If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    #Loop through the request.form object and update the productions attributes. Note: Be cautions of the data types to avoid errors.
    #add and commit the updated production 
    #Create and return the response
  
#12. Delete
    #Create a delete method, pass it self and the id
    #Query the Production 
    #If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    #delete the production and commit 
    #create a response with the status of 204 and return the response 


#13. Use the @app.errorhandler() decorator to handle Not Found
    #Create the decorator and pass it NotFound
    #Use make_response to create a response with a message and the status 404
    #return the response
    
# To run the file as a script
if __name__ == '__main__':
    app.run(port=4000, debug=True)