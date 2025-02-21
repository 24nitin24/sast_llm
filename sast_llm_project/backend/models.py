from backend import db, bcrypt
from flask_jwt_extended import create_access_token
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="user")  # Can be 'admin' or 'user'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def generate_token(self):
        return create_access_token(identity={"id": self.id, "role": self.role})

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    threat_scenarios = db.Column(db.Integer, default=0)
    security_test_cases = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)  # Markdown content
    team_members = db.Column(db.String(255), nullable=True)  # Names of team members
    deadline = db.Column(db.String(50), nullable=True)  # Deadline Date
    priority = db.Column(db.String(50), nullable=True)  # High, Medium, Low
    category = db.Column(db.String(100), nullable=True)  # Category Type
    image_path = db.Column(db.String(255), nullable=True)  # Uploaded image path