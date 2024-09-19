from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Car(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    modifications = db.Column(db.String)
    img = db.Column(db.String)
    
    def __init__(self ,make, model, year, modifications, img):
        self.make = make
        self.model = model
        self.year = year
        self.modifications = modifications
        self.img = img


#3
    @classmethod
    def show_all_cars(cls):
        cls.query.all()
    

