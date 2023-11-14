
from flask_sqlalchemy import SQLAlchemy
#1. Import `SerializerMixin` from `sqlalchemy_serializer`
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

# 2. Pass `SerializerMixin` to `Productions`
class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    crew_members = db.relationship("CrewMember", backref='production')

    #3. Create a serialize rule that will help add our `crew_members` to the response and remove created_at and updated_at.
    #Demo serialize_only by only allowing title to be included in the response
    #once done remove or comment the serialize_only line.
    serialize_rules = ('-crew_members.production',)

    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>'

#4.#Review: create a new CrewMember class with name, role, created_at, updated_at, and a foreign key to the production table
class CrewMember(db.Model, SerializerMixin):
    __tablename__ = "crew_members"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    #4. Pass `SerializerMixin` to `CrewMember`
    #6. Create a serialize rule that will help add our `production` to the response.

    serialize_rules = ('-production.crew_members',)
      

 #7.Navigate back to `app.py` for further steps.