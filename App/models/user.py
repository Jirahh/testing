from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask import jsonify

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    profile = db.relationship("Profile", backref="owner", uselist=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile-id': self.profile.toJSON(),
        }
    

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
