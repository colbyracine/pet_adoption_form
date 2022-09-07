from flask_sqlalchemy import SQLAlchemy

generic_photo = "https://t4.ftcdn.net/jpg/00/89/55/15/360_F_89551596_LdHAZRwz3i4EM4J0NHNHy2hEUYDfXc0j.jpg"

db = SQLAlchemy()


    

# MODELS BELOW

class Pet(db.Model):
    """Pet Adoption Model"""
    
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    def image_url(self):
        """return image"""
        
        return self.photo_url or generic_photo
    

def connect_db(app):
    """Connect to Flask app"""
    db.app = app
    db.init_app(app)