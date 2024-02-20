#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app
from models import db, Production

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`

# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
    
# 8.✅ Create a query to delete all existing records from Production 
    Production.query.delete()
   
# 9.✅ Create some seeds for production and commit them to the database. 
    productions = []
    p1 = Production(title="Hamlet", genre="Drama", budget=100000.0, image="https://cdn.kobo.com/book-images/5fc4252b-1c4f-40ef-9975-22982c94f12c/1200/1200/False/hamlet-prince-of-denmark-23.jpg", description="Hamlet is melancholy, bitter, and cynical, full of hatred for his uncle's scheming and disgust for his mother's sexuality. A reflective and thoughtful young man who has studied at the University of Wittenberg, Hamlet is often indecisive and hesitant, but at other times prone to rash and impulsive acts.", director="Bill Shakespeare", ongoing=False)
    p2 = Production(title="Hamilton", genre="Musical", budget=400000.0, image="https://www.foxtheatre.org/assets/img/ATL_2324_FOXGraphics_Web_HAM630x580-b9cc36d541.png", description="A revolutionary story of passion, unstoppable ambition, and the dawn of a new nation. HAMILTON is the epic saga that follows the rise of Founding Father Alexander Hamilton as he fights for honour, love, and a legacy that would shape the course of a nation.", director="Lin-Manuel", ongoing=True)
    productions.append(p1)
    productions.append(p2)
    db.session.add_all(productions)
    db.session.commit()
# 10.✅ Run in terminal:
    # `python seed.py`

# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
    
# 12.✅ Navigate back to app.py  
    
    